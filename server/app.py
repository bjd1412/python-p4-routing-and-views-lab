#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:param>')
def print_string(param):
    print(param)
    return param

@app.route('/count/<int:param>')
def count(param):
    r = ""
    for i in range(param):
        r += str(i) + '\n'
    return r

@app.route('/math/<int:num1>/<string:op>/<int:num2>')
def math(num1, op, num2):
    themath = None
    if op == '+':
        themath = num1 + num2
    elif op == '-':
        themath = num1 - num2
    elif op == '*':
        themath = num1 * num2
    elif op == 'div':
        themath = num1 / num2
    elif op == '%':
        themath = num1 % num2

    return str(themath)

    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
