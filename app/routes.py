from app import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "Robin"}
    posts = [
        {
            "author": {"username": "John"},
            "post": "Lovely weather here in Alaska"
         },
        {
            "author": {"username": "Thor"},
            "post": "Wakanda forever"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)
