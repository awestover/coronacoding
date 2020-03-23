from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route("/helloWorld")
def helloWorld():
    return "<h1>hello world</h1> <p>this is a paragraph</p>"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/data", methods=("POST",))
def data():
    print(request.form)
    return "I see you " + request.form["username"]

app.run(debug=True, host='0.0.0.0')

