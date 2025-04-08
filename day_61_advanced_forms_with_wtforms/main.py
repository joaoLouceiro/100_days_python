from ensurepip import bootstrap

from wtforms import Form, StringField, PasswordField, SubmitField
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap5
from wtforms.validators import Email, Length, DataRequired, ValidationError
from flask import Flask, render_template, request

app = Flask(__name__)

app.secret_key = "my secret key"

bootstrap = Bootstrap5(app)

class LoginForm(FlaskForm):
    email = StringField('Email', [
        DataRequired(message="Required Field"),
        Length(min=6, message='Little short for an email address?'),
        Email(message='That\'s not a valid email address.')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message="Required Field"),
        Length(min=6)
    ])
    submit = SubmitField(label="Log In")
    def validate_email(self, field):
        if field.data != "admin@email.com":
            raise ValidationError("Invalid email")
    def validate_password(self, field):
        if field.data != "123456":
            raise ValidationError("Invalid password")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['post', 'get'])
def login():
    login_form = LoginForm()
    if request.method == 'GET':
        return render_template('login.html', form=login_form)
    elif request.method == 'POST' and login_form.validate_on_submit():
        return render_template("success.html")
    else:
        return render_template("denied.html")

if __name__ == '__main__':
    app.run(debug=True)
