#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(port=5552, debug=True)

@app.route('/')
def index():
    title = "Python Operations with Flask Routing and Views"
    return f'<h1>{title}</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)  

    paragraph = param
    return paragraph

@app.route('/count/<int:param>')
def count(param):
    numbers = "\n".join(str(i) for i in range(param+1))
    return numbers

@app.route('/math/<int:num1>/<operation>/<int:num2>')
def math(num1, operation, num2):
    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return "Division by zero is not allowed."
    elif operation == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations are +, -, *, div, and %."

    return str(result)
  
