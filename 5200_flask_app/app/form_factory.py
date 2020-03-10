#form factory
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired
from app.valid_rules import RULE_REQUIRED_FIELDS, RULE_OPTIONAL_FIELDS, RULE_VALID_PROVINCES

form_fields = {'Building Number',
               'Floor',
               'County',
               'Street 1',
               'City',
               'Postcode',
               'Province',
               'Post Office Code',
               'Building Name',
               'Block',
               'District',
               'Country',
               'State',
               'Apt Number',
               'House', 'Street 2', 'Entrance', 'Zone', 'Department'}

def country_form_factory(country):
    if country in RULE_OPTIONAL_FIELDS.keys():
        all_fields = set(RULE_REQUIRED_FIELDS[country] + RULE_OPTIONAL_FIELDS[country])
    else:
        all_fields = set(RULE_REQUIRED_FIELDS[country])

    print(all_fields)
    valid_provinces = False
    if country in RULE_VALID_PROVINCES.keys():
        valid_provinces = RULE_VALID_PROVINCES[country]

    class FormGenerator(FlaskForm):
        submit = SubmitField('submit')

    for field in all_fields:
        if field in {'Building Number', 'Block', 'Apt Number', 'House', 'Post Office Code', 'Floor', 'Zone'}:
            setattr(FormGenerator, str.replace(field, ' ', '_'), IntegerField(field))
        if field in {'Street 1', 'Street 2', 'Entrance', 'City', 'Building Name', 'District', 'Department', 'County'}:
            setattr(FormGenerator, str.replace(field, ' ', '_'), StringField(field))
        if field in {'State', 'Province'}:
            if valid_provinces:
                setattr(FormGenerator, str.replace(field, ' ', '_'),  SelectField(field, choices=[(state, state) for state in RULE_VALID_PROVINCES[country]]))
            else:
                setattr(FormGenerator, str.replace(field, ' ', '_'), StringField(field))
        if field == 'Postcode':
            setattr(FormGenerator, str.replace(field, ' ', '_'), StringField(field))
    all_fields = [str.replace(field, ' ', '_') for field in all_fields]
    all_fields.remove('Country')
    all_fields.append('submit')
    return (FormGenerator(), all_fields)

