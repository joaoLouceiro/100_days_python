from flask import Flask, render_template
import requests

app = Flask(__name__)
fake_blogs = "https://api.npoint.io/88422ea7549c6946b124"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def guess(name):
    params = {"name" : name}
    age = requests.get("https://api.agify.io?", params=params).json()["age"]
    gender = requests.get("https://api.genderize.io?", params=params).json()["gender"]
    return render_template("guess.html", name=name, age=age, gender=gender)

@app.route("/blog")
def blog():
    blog_posts = get_posts()
    return render_template("blog.html", blog_posts=blog_posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    blog_posts = get_posts()
    current_post = blog_posts[post_id]
    return render_template("post.html", post=current_post)


def get_posts():
    res = requests.get(fake_blogs)
    res.raise_for_status()
    return res.json()

app.run(debug=True)