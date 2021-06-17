from flask import Flask, render_template, request
import math

app = Flask(__name__)

def plus(input1,input2):
    sum=float(input1)+float(input2)
    return str(sum)
def minus(input1,input2):
    minus1=float(input1)-float(input2)
    return str(minus1)
def root(input1):
    root=math.sqrt(float(input1))
    return str(root)
def division(input1,input2):
    return input1/input2
def multiply(input1,input2):
    return input1*input2
def square(input1):
    return input1*input1


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/',methods=['POST'])
def calculate():
    firstNum = request.form['firstNumber']
    secondNum = request.form['secondNumber']
    operator = request.form['operator']

    if operator=='+':
        result = plus(firstNum, secondNum)
    elif operator=='-':
        result=minus(firstNum,secondNum)
    elif operator=="/":
        result=division(firstNum,secondNum)
    elif operator=="*":
        result=multiply(firstNum,secondNum)
    elif operator=="^2":
        result=square(firstNum)
    elif operator=='√':
        result=root(firstNum)




    return render_template('index.html',expr=result)




if __name__ == "__main__":
    app.run(debug=True)