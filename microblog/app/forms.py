from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
import sqlalchemy as sa 
from app import db 
from app.models import User 

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me")
    submit = SubmitField("sign in")

class RegistrationForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("password", validators=[DataRequired()])
    password2 = PasswordField("repeat password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        # check in database if username already exists 
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None : 
            raise ValidationError("Username already in use")
        
    def validate_email(self, email): 
        # check in database if email already exists 
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None : 
            raise ValidationError("Email already in use")

