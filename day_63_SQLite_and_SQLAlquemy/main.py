from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-collection.db"
db = SQLAlchemy(model_class=Base)

db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True)
    author: Mapped[str]
    ranking: Mapped[int]

with app.app_context():
    db.create_all()


@app.route('/')
def home():
    with app.app_context():
        result = db.session.execute(db.select(Book)).scalars()
        return render_template("index.html", books=result)

@app.route("/add")
def add():
    return render_template("add.html")

@app.post("/add")
def add_book():
    form = request.form
    book = Book(
        title=form["title"],
        author=form["author"],
        ranking=form["rating"]
    )
    db.session.add(book)
    db.session.commit()
    return redirect("/")

@app.route("/edit", methods=['get', 'post'])
def edit_book():
    book_id = request.args.get("id")
    book = get_book_by_id(book_id)
    if request.method == 'GET':
        return render_template("edit.html", book=book)
    else:
        book.ranking = request.form["new_rating"]
        db.session.commit()
        return redirect(url_for("home"))

@app.route("/delete")
def delete():
    book_id = request.args.get("id")
    book = get_book_by_id(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


def get_book_by_id(book_id):
    with app.app_context():
        return db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()

if __name__ == "__main__":
    app.run(debug=True)

