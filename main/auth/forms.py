from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,Length,EqualTo

class LoginForm(FlaskForm):
    name=StringField(label="Name", validators=[DataRequired()])
    password=PasswordField(label="Password",validators=[DataRequired()])
    submit=SubmitField(label="Submit")

class SigupForm(FlaskForm):
    name=StringField(label="Name", validators=[DataRequired()])
    password=PasswordField(label="Password",validators=[DataRequired(),Length(min=6)])
    confirm_password=PasswordField(label="Comfirm Password",validators=[DataRequired(),EqualTo(password)])
    submit=SubmitField(label="Register")
