from flask import Flask, jsonify
from FromIntToTwit import *
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getTwits/<title>')
def getTwitsWEB(title):
    print("Request is received")
    arr = getTwits(title)
    ans = dict()
    ans["time"] = arr[0]
    ans["forked"] = str(arr[1])
    ans["reposted"] = str(arr[2])
    ans["liked"] = str(arr[3])
    return jsonify(ans)