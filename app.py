from flask import Flask,jsonify
import requests
from data import getdata


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
    return "API is working fine"

@app.route("/<string>")
def nat(string):
	x=getdata(string)
	return x


if __name__ == "__main__":
    app.debug = True
    app.run()