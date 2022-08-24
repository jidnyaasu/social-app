from flask import render_template, flash, redirect, request, url_for
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, \
    ResetPasswordForm, PasswordChangeForm
from werkzeug.urls import url_parse
from app import db
from app.auth import bp
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from app.auth.email import send_password_reset_email
from flask_babel import _


@bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_("Invalid username or password"))
            return redirect(url_for("auth.login"))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get("next")
        if not next_page or url_parse(next_page).netloc != "":
            next_page = url_for("index")
        return redirect(next_page)
    return render_template("auth/login.html", title="Sign In", form=form)


@bp.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("index"))


@bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_("Congratulations! You are now a registered user!"))
        return redirect(url_for("auth.login"))
    return render_template("auth/register.html", title="Register", form=form)


@bp.route("/change_password", methods=["GET", "POST"])
@login_required
def change_password():
    form = PasswordChangeForm()
    if form.validate_on_submit():
        if current_user.check_password(form.current_password.data):
            if current_user.check_password(form.password.data):
                flash(_("New password can't be same as current password"))
            else:
                current_user.set_password(form.password.data)
                db.session.commit()
                flash(_("Password changed!"))
                return redirect(url_for("edit_profile"))
        else:
            flash(_("Enter correct password"))
    return render_template("auth/change_password.html", title="Change Password", form=form)


@bp.route("/reset_password_request", methods=["GET", "POST"])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash(_("Check your email for the instructions to reset your account password"))
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password_request.html", title="Reset Password", form=form)


@bp.route("/reset_password/<token>", methods=["GET", "POST"])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for("index"))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash(_("Your password has been reset."))
        return redirect(url_for("auth.login"))
    return render_template("auth/reset_password.html", form=form)
