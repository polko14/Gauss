from flask import Flask, render_template, request
import json
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/square")
def square():
    n=int(request.args.get("number"))
    return json.dumps({
        "result":str(n**2)
        })
