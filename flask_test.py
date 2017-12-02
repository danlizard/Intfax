from flask import Flask, jsonify
from FromIntToTwit import *
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/getTwits/<title>', methods=['POST'])
def getTwitsWEB(title):
    print("Request is received")
    arr = getTwits(request.form["title"])
    ans = dict()
    ans["time"] = arr[0]
    ans["forked"] = str(arr[1])
    ans["reposted"] = str(arr[2])
    ans["liked"] = str(arr[3])
    return jsonify(ans)