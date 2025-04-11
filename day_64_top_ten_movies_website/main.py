import os

from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.numeric import DecimalField
from wtforms.validators import DataRequired, NumberRange
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

TMDB_TOKEN=os.getenv("TMDB_TOKEN")

tmdb_headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {TMDB_TOKEN}"
}


# CREATE DB
class Base(DeclarativeBase):
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///my_top_ten"
db = SQLAlchemy(model_class=Base)

db.init_app(app)

# CREATE TABLE
class Movie(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    year: Mapped[int] = mapped_column(nullable=False)
    description : Mapped[str] = mapped_column()
    rating: Mapped[float] = mapped_column(nullable=True)
    ranking: Mapped[int] = mapped_column(nullable=True)
    review: Mapped[int] = mapped_column()
    img_url: Mapped[str] = mapped_column(unique=True)


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    with app.app_context():
        movie_list = db.session.execute(db.select(Movie).order_by(Movie.ranking.desc())).scalars()
        return render_template("index.html", movie_list=movie_list)

@app.route("/edit", methods=['get', 'post'])
def edit():
    movie_id = request.args.get("movie_id")
    form = EditForm()
    with app.app_context():
        movie: Movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        if form.validate_on_submit():
            movie.rating = form.rating.data
            movie.review = form.review.data
            db.session.commit()
            update_ranking()
            return redirect('/')
        return render_template("edit.html", movie=movie, form=form)


class EditForm(FlaskForm):
    rating = DecimalField(label="Your rating out of 10", validators=[DataRequired(), NumberRange(min=0, max=10)])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField()

@app.route("/delete")
def delete():
    movie_id = request.args.get("movie_id")
    with app.app_context():
        movie: Movie = db.session.execute(db.select(Movie).where(Movie.id == movie_id)).scalar()
        db.session.delete(movie)
        db.session.commit()
        return redirect('/')

@app.route("/add", methods=['post', 'get'])
def add():
    form = AddMovieForm()
    if form.validate_on_submit():
        import requests
        url = "https://api.themoviedb.org/3/search/movie?"
        params={
            "query": form.title.data
        }
        response = requests.get(url, headers=tmdb_headers, params=params)
        response.raise_for_status()
        return render_template("select.html", movie_list=response.json()["results"])

    return render_template("add.html", form=form)

class AddMovieForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField()

@app.get("/select")
def select():
    movie_id = request.args.get("movie_id")
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?language=en-US"

    response = requests.get(url, headers=tmdb_headers)
    response.raise_for_status()
    res = response.json()
    movie = Movie(
        title=res["original_title"],
        description=res["overview"],
        img_url=f"https://image.tmdb.org/t/p/w500/{res['poster_path']}",
        year=res["original_title"].split("-")[0]
    )
    with app.app_context():
        db.session.add(movie)
        db.session.commit()
        new_movie_entity = db.session.execute(db.select(Movie).where(Movie.title == res["original_title"])).scalar()

    return redirect(url_for('edit', movie_id=new_movie_entity.id))

def update_ranking():
    with app.app_context():
        movie_list = db.session.execute(db.select(Movie).order_by(Movie.rating.desc())).scalars()
        for index,movie in enumerate(movie_list):
            movie.ranking = index + 1
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
