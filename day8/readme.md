---
title: day8
author: Alek
---


In the terminal, type `python3 app.py`
Go to [localhost:5000](localhost:5000) in your web browser.

Setup the project:
```sh
cd Desktop/coronacoding/day8
touch app.py 
mkdir static
mkdir templates
touch templates/index.html
```
open the project (`day8`) in sublime.

Put the following in `app.py`
```python
from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    return "<h1>hello world</h1> <p>this is a paragraph</p>"

app.run(debug=True, host='0.0.0.0')
```

```sh
python3 -m http.server
```
