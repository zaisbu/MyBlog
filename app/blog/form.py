from wtforms import Form, StringField, IntegerField
from wtforms.validators import DataRequired


class Blogform(Form):
    blogtitel = StringField('Blog-Titel', validators = [DataRequired()])
    kategorie = IntegerField('Kategorie', validators = [DataRequired()])
    text = StringField('Text', validators = [DataRequired()])
