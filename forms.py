from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtf.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm)
    username = StringField('username', validators=[DataRequired(), Length(min=2, max=16)])
    email = StringField('email', validators=[DataRequired(), Email()])
    password = PasswordField('password', validators=[DataRequired()])
    confirm = PasswordField('confirm password', validators=[DataRequired(), EqualTo('pasword')])

