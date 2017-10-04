from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/")
def index():
    error = request.args.get("error")
    return render_template('index.html', error=error and cgi.escape(error, quote=true) )