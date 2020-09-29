from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired


class Kategorieform(Form):
    name = StringField('Kategorie', validators = [DataRequired()])
