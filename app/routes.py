from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm


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


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login requested for user {form.username.data}, remember_me = {form.remember_me.data}")
        return redirect(url_for("index"))
    return render_template("login.html", title="Sign In", form=form)
