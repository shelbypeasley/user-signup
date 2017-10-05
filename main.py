from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/welcome", methods=["POST"])
def welcome():
    if username == "" or username < 3 or username > 20:
        error = "username is not valid"
        return redirect("/?error=" + error)
    if password == "" or password < 3 or username > 20:
        error = "password is not valid"
        return redirect("/?error=" + error)
    if password != verify:
        error = "passwords do not match"
        return redirect("/?error=" + error)

    return render_template('welcome.html', username=username)

@app.route("/")
def index():
    error = request.args.get("error")
    return render_template('index.html', error=error and cgi.escape(error, quote=true))

if __name__ == "__main__":
    app.run()