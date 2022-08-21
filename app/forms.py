from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo, Length
from app.models import User
from flask_babel import lazy_gettext as _l, _


class LoginForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    remember_me = BooleanField(_l("Remember me"))
    submit = SubmitField(_l("Sign In"))


class RegistrationForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    password = PasswordField(_l("Password"), validators=[DataRequired()])
    password2 = PasswordField(_l("Confirm Password"), validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField(_l("Register"))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_("Please use a different username"))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_("Please use a different email address"))


class PostForm(FlaskForm):
    post = TextAreaField(_l("Write something:"), validators=[DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l("Post"))


class EditProfileForm(FlaskForm):
    username = StringField(_l("username"), validators=[DataRequired()])
    about_me = TextAreaField(_l("About me"), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l("Submit"))

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_("Please use a different username"))


class Emptyform(FlaskForm):
    submit = SubmitField("Submit")


class RestPasswordRequestForm(FlaskForm):
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    submit = SubmitField(_l("Request Password Reset"))


class PasswordChangeForm(FlaskForm):
    current_password = PasswordField(_l("Enter Current Password"), validators=[DataRequired()])
    password = PasswordField(_l("Enter New Password"), validators=[DataRequired()])
    password2 = PasswordField(
        _l("Confirm New Password"), validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField(_l("Change Password"))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l("Enter New Password"), validators=[DataRequired()])
    password2 = PasswordField(
        _l("Confirm New Password"), validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField(_l("Reset"))
