from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, DateField, SubmitField
from wtforms.validators import DataRequired

class TransactionForm(FlaskForm):
    amount = DecimalField('Amount', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired()])
    date = DateField('Date', format='%Y-%m-%d', validators=[DataRequired()])
    submit = SubmitField('Add Transaction')
