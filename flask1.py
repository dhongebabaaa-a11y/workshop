from flask import Flask

app=Flask(__name__)

@app.route("/")
def home():
    return "Python world in good"

@app.route("/greet/<name>")
def greet(name):
    return f"hello,{name}!"

@app.route("/add/<int:a>/<int:b>")
def add(a , b):
    return f"{a}  +   {b}={a+b}"

@app.route("/sub/<int:a>/<int:b>")
def sub(a , b):
    return f"{a}  -   {b}={a-b}"

if __name__=="__main__":
    app.run(debug=True)