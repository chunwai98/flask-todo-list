from flask_wtf import FlaskForm
from wtforms import StringField,BooleanField,SubmitField
from wtforms.validators import InputRequired

class TodoForm(FlaskForm):
    task=StringField(label="Task",validators=[InputRequired()],default=None)
    completed=BooleanField(label="Completed",default=False)
    submit=SubmitField(label="Add")

