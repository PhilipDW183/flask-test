from core.calculator import calculator
from flask import render_template, url_for, redirect, request
from core.calculator.forms import CalculatorForm

base_path = "/calculator"

@calculator.route(base_path, methods=("GET", "POST"))
def calculator_index():
    form = CalculatorForm()
    if form.validate_on_submit():
            first_input = form.input1.data
            second_input = form.input2.data
            operation = form.operation.data

            try:
                input1 = float(first_input)
                input2 = float(second_input)

                if operation == "+":
                    result = input1 + input2
                elif operation == "-":
                    result = input1 - input2
                elif operation == "*":
                    result = input1 * input2
                else:
                    if (input1==0 and input2 ==0):
                        result = 0
                    else:
                        result = input1 / input2
                return render_template("calculator.html",
                    form = form,
                    input1 = input1,
                    input2 = input2,
                    operation = operation,
                    result = result,
                    calculation_success=True)
            except ZeroDivisionError:
                return render_template("calculator.html",
                    form=form,
                    input1 = input1,
                    input2 = input2,
                    operation = operation,
                    result = "Bad input",
                    calculation_success=False,
                    error="You cannot divide by zero")
    return render_template("calculator.html", form=form)

