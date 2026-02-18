from flask import Flask
import pickle


app = Flask(__name__)

@app.route("/") #base url
def hello_world():
    return "<h2> Hello, Welcome to my World! </h2>"


@app.route("/ping", methods=['GET'])
def ping():
    return {"message": "Hi there, I'm working!!"}