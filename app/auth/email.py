from flask import render_template, current_app
from flask_babel import _
from app.email import send_mail


def send_password_reset_email(user):
    token = user.get_reset_password_token()
    send_mail(_("[Social App] Reset Your Password"),
              sender=current_app.config["ADMINS"][0],
              recipients=[user.email],
              text_body=render_template("email/reset_password_mail.txt",
                                        user=user, token=token),
              html_body=render_template("email/reset_password_mail.html",
                                        user=user, token=token))
