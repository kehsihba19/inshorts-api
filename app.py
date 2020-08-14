from flask import Flask,jsonify
import requests
from data import getdata


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
    x={"all":"https://inshorts-news.vercel.app/all","national":"https://inshorts-news.vercel.app/national","business":"https://inshorts-news.vercel.app/business","sports":"https://inshorts-news.vercel.app/sports","world":"https://inshorts-news.vercel.app/world","politics":"https://inshorts-news.vercel.app/politics","technology":"https://inshorts-news.vercel.app/technology","startup":"https://inshorts-news.vercel.app/startup","entertainment":"https://inshorts-news.vercel.app/entertainment","science":"https://inshorts-news.vercel.app/science","automobile":"https://inshorts-news.vercel.app/automobile"}
    return x

@app.route("/<string>")
def nat(string):
	x=getdata(string)
	return x


if __name__ == "__main__":
    #app.debug = True
    app.run()
