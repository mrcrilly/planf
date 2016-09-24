
from flask_wtf import Form
from wtforms import Form, StringField, FieldList, FormField
from wtforms.validators import DataRequired

class IncomeForm(Form):
    name = StringField('name', validators=[DataRequired()])
    amount = StringField('amount', validators=[DataRequired()])

class IncomesCollection(Form):
    incomes = FieldList(FormField(IncomeForm), min_entries=1)