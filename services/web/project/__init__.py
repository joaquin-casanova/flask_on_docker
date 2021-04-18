from flask import Flask, jsonify


#instanciamos la app
app = Flask(__name__)


@app.route('/')
def hello_wold():
    return jsonify(hello = "world")