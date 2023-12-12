from flask import Flask, request,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to flask practice"
@app.route('/calc',methods=["GET"])
def math_operator():
    operator=request.json["operator"]
    number1=request.json["number1"]
    number2=request.json["number2"]

    if operator=="add":
        result=number1+number2
    elif operator=="multiplication":
        result=number1*number2
    elif operator=="division":
        result=number1/number2
    else:
        result=number1-number2
    return result











if __name__=='__main__':
    app.run()