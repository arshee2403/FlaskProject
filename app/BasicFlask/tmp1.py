from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def index():
    
    lists=[{'user':'Dhiraj'},{'username':'Daniel','body':'Beautiful day in SriLanka'},
           {'username':'Amar','body':'Tiger Zinda hai was cool'}]
    
    
    return render_template('tmp.html',name=lists)
if __name__=='__main__':
    app.run(debug = True)
