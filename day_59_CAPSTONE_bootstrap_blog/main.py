from flask import Flask,render_template
import requests

req = requests.get("https://api.npoint.io/9f957a6f1c4737ce0926")
req.raise_for_status()
res = req.json()

app = Flask(__name__)

@app.route("/")
def home():
    header = {
        "heading": "Clean Blog",
        "subheading": "A Blog Theme by Start Bootstrap",
        "image": "/static/assets/img/home-bg.jpg"
    }
    return render_template("index.html", header=header, posts=res)

@app.route("/about")
def about():
    header = {
        "heading": "About Me",
        "subheading": "This is what I do.",
        "image": "/static/assets/img/about-bg.jpg"
    }
    return render_template("about.html", header=header)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next(p for p in res if p["id"] == post_id)
    header = {
        "heading": post["title"],
        "subheading": post["subtitle"],
        "image": post["image_url"],
    }
    return render_template("post.html", header=header, post=post)

@app.route("/contact")
def contact():
    header = {
        "heading": "Contact Me",
        "subheading": "Have questions? I have answers.",
        "image": "/static/assets/img/contact-bg.jpg"
    }
    return render_template("contact.html", header=header)

if __name__ == "__main__":
    app.run(debug=True)
