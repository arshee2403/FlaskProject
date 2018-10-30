from flask import Flask
app=Flask(__name__)

@app.route("/hi/<name>")

def string1(name):
    return "About! %s" %name
@app.route("/hi1/<int:no>")
def int1(no):
    return "About! %d" %no
@app.route("/hi2/<float:no1>")
def float1(no1):
    return "About! %f" %no1

if __name__=="__main__":
    app.run(debug=True)
