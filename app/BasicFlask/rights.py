from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/admin")
def hello_admin():
    return "Administration area,gusts not allowed"
@app.route("/guest/<name>")
def hello_guest(name):
    return "Guest user %s not having admin rights"%name

@app.route("/user/<user>")
def hello_user(user):
    if user=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',name=user))
    
        
if __name__=="__main__":
    app.run(debug=True)
