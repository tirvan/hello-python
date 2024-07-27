import os

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    statement = os.environ['APPENV'] + ": Hello world - v3.0\n\n"
    return statement

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
