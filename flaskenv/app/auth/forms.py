from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from app.auth.models import User


def email_exists(form,field):
        email = User.query.filter_by(user_email=field.data).first()
        if email:
                raise ValidationError('Email already exists')
        


class RegistrationForm(FlaskForm):
        name = StringField('Whats your name',validators=[DataRequired(),Length(3,15, message='Between 3 to 15 characters')])
        email = StringField('Enter your email', validators= [DataRequired(), Email(), email_exists])
        password = PasswordField('Password',validators= [DataRequired(), Length(5), EqualTo('confirm', message='Password must match')])
        confirm = PasswordField('Confirm',validators= [DataRequired()])
        submit = SubmitField('Register')

class LoginForm(FlaskForm):
        email = StringField(validators= [DataRequired(), Email()])
        password = PasswordField(validators= [DataRequired()])
        stay_loggein = BooleanField('stay logged-in')
        login = SubmitField('LogIn')
