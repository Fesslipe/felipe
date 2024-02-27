from flask import Flask, request, make_response, redirect, abort, render_template, request
app = Flask(__name__);

@app.route('/')
def index():
    return render_template("index.html");

@app.route('/user/<name>/<enrollment>/<college>')
def user(name, enrollment, college):
    return render_template("user.html").format(name, enrollment, college);

@app.route('/contextorequisicao')
def requestContext():
    userAgent = request.headers.get("User-Agent")
    userIp = request.headers.get("host")
    appHost = request.headers.get("Referer")
    return render_template("requestContext.html").format(userAgent, userIp, appHost)