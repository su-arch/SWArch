#form factory
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired




### TWO examples of formFactories from flask
class FormFactory(FlaskForm):
    radio_fields = RadioField('', choices=[])
    submit = SubmitField('submit')

    def __init__(self, label, choices):
        super().__init__()
        self.radio_fields.choices = label
        self.radio_fields.choices = choices


def FormFactory(n, **kwargs):
    class FormGenerator(FlaskForm):
        submit = SubmitField('submit')

    for i in range(n):
        setattr(FormGenerator, RadioField(args[i][0], choices=args[i][1])

    return FormGenerator()


def form_factory():
    return FlaskForm