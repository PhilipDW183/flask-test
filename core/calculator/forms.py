from flask_wtf import FlaskForm
from wtforms import (SelectField,  DecimalField, SubmitField)
from wtforms.validators import InputRequired

class CalculatorForm(FlaskForm):
    input1 = DecimalField("Input 1", validators = [InputRequired()])
    input2 = DecimalField("Input 2", validators = [InputRequired()])
    operation = SelectField("Operation", choices=[("+", "Addition"), 
        ("-", "Subtraction"),
        ("/", "Division"),
        ("*", "Multiplication"),
        ("%", "Remainder"),
        ("//", "Floor division")],
        validators = [InputRequired()])
    submit = SubmitField("Calculate")