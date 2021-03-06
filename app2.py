# -*- coding: utf-8 -*-
"""app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1PEiUIhZxr3dhmYQCRMiLVJRS6myCoP3C
"""

import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
#scaling=pickle.load(open('scaling.pkl','rb'))
@app.route('/')
def home():
  return render_template('index.html')
@app.route('/predict',methods=['POST'])
def predict():
  int_features=[int(x) for x in request.form.values()]
  final_features=[np.array(int_features)]
  #final_features=scaling.transform(final_features)
  prediction=model.predict(final_features)
  output=prediction
  if(output.sum()==1):
    output='Yes'
  else:
    output='No'
  return render_template('index.html',prediction_text='Customer purchase status: '+str(output))

if __name__ =="__main__":
  app.run(debug=True)