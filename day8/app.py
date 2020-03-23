from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>hello world</h1> <p>this is a paragraph</p>"

app.run(debug=True, host='0.0.0.0')

