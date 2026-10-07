# import flask
from flask.templating import render_template
from flask import Flask, request

#initiate flask
app = Flask(__name__)

# Define routes first of all default route is/
@app.route('/')
def home():
    return "Web development in Python."

@app.route("/greet/<name>")
def greet(name):
    return f"Hello, {name}!"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/sub/<int:a>/<int:b>")
def sub(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/template")
def template():
    return render_template("page.html", name="Hello Cosmos")


@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method=="POST":
      name=request.form["name"]
      return f"hello, {name}!"
    return render_template("form.html")


# run the app
if __name__ == "__main__":
    app.run(debug=True)
