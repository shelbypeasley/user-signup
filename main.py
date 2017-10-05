from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=["POST"])
def welcome():
    username = request.form['username']
    if username == "" or len(username) < 3 or len(username) > 20:
        error = "username is not valid"
        return redirect("/?error=" + error)
    password = request.form['password']
    if password == "" or len(password) < 3 or len(password) > 20:
        error = "password is not valid"
        return redirect("/?error=" + error)
    verify = request.form['verify']
    if password != verify:
        error = "passwords do not match"
        return redirect("/?error=" + error)

    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    error = request.args.get("error")
    return render_template('index.html', error=error and cgi.escape(error, quote=True))

if __name__ == "__main__":
    app.run()