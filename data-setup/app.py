# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)

# Root
@app.route("/")
def index():
    return "data setup"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8090, debug=True)
