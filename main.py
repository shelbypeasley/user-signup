from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route("/", methods=["POST"])
def welcome():
    error1 = ""
    error2 = ""
    error3 = ""
    error4 = ""
    username = request.form['username']
    if username == "" or len(username) < 3 or len(username) > 20 or " " in username:
        error1 = "username is not valid"
    
    password = request.form['password']
    if password == "" or len(password) < 3 or len(password) > 20 or " " in username:
        error2 = "password is not valid"
        
    verify = request.form['verify']
    if verify == "":
        error3 = "must verify password"
        
    if verify != password:
        error3 = "passwords do not match"
        
    email = request.form['email']
    if "@" not in email or "." not in email or " " in email or len(email) < 3 or len(email) > 20:
        error4 = "not a valid email address"
    
    if email == "":
        error4 = ""
        
    if error1 or error2 or error3 or error4:
        return render_template('index.html', username=username, password=password, error1=error1, error2=error2, error3=error3, error4=error4)
    
    else:
        return render_template('welcome.html', username=username)

@app.route("/")
def index():
    error = request.args.get("error")
    return render_template('index.html', error=error and cgi.escape(error, quote=True))

if __name__ == "__main__":
    app.run()