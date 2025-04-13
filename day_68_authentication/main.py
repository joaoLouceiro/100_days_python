from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-goes-here'

# CREATE DATABASE


class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# CREATE TABLE IN DB

class User(UserMixin, db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


with app.app_context():
    db.create_all()


login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return db.get_or_404(User, user_id)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register')
def register():
    return render_template("register.html")

@app.post('/register')
def add_user():
    form = request.form
    new_user = User(
        email=form.get("email"),
        name=form.get("name"),
        password=get_hashed_pass(form.get("password"))
    )
    user = db.session.execute(db.select(User).where(User.email == form.get("email"))).scalar()
    if user:
        flash("Email in use")
        return redirect('register')
    else:
        db.session.add(new_user)
        db.session.commit()
        return redirect('login')


@app.route('/login', methods=['get', 'post'])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        user = db.session.execute(db.select(User).where(User.email == email)).scalar()
        if user and check_password_hash(user.password, request.form.get("password")):
            login_user(user)
            return redirect(url_for('secrets'))
        else:
            flash("Invalid email or password")
    return render_template("login.html")

@app.route('/secrets')
@login_required
def secrets():
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files/', 'cheat_sheet.pdf')

def get_hashed_pass(password):
    return generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)

if __name__ == "__main__":
    app.run(debug=True)
