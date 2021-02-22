from flask import Flask,render_template,request,send_file,send_from_directory
import numpy as np


app = Flask(__name__,static_folder='static',template_folder='templates')

@app.route('/')
def home():
      return render_template("index.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
  if request.method=='POST':
    return render_template("index.html")

  if request.method=='GET':
    return render_template("index.html")

     
if __name__=='__main__':
    app.run(debug=False,threaded=False)
