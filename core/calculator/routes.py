from core.calculator import calculator
from flask import render_template, url_for, redirect, request

base_path = "/calculator"

@calculator.route(base_path)
def calculator_index():
    return render_template("calculator.html")

@calculator.route(f"{base_path}/calculate", methods=["POST"])
def calculate():
    first_input = request.form.get("input1")
    second_input = request.form.get("input2")
    operation = request.form.get("operation")

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
            input1 = input1,
            input2 = input2,
            operation = operation,
            result = result,
            calculation_success=True)
    except ZeroDivisionError:
        return render_template("calculator.html",
            input1 = input1,
            input2 = input2,
            operation = operation,
            result = "Bad input",
            calculation_success=False,
            error="You cannot divide by zero")
    except ValueError:
        return render_template("calculator.html",
            input1 = first_input,
            input2 = second_input,
            operation = operation,
            result = "Bad input",
            calculation_success=False,
            error="Operation cannot be performed with input provided")


