from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    with open("root.html") as page:
        return page.read()

app.route()
if __name__ == "__main__":
    app.run(debug=True)
