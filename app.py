from flask import Flask,request,render_template
import pandas as pd
import numpy as np
from sklearn.externals import joblib

app=Flask(__name__)

model=joblib.load(open('model.pkl','rb'))

@app.route('/')
def home():
  return render_template('index.html')

@app.route('/forecast',methods=['POST'])
def predict():
  '''
    For rendering prediction result on index.html
  '''
  try:
    date=request.form['date']
    last_date='2016-11-30'
    mydates=pd.date_range(last_date,date).tolist()
    last_temp=22.5
    pred=model.forecast(model.y,steps=len(mydates))
    pred_steps=pd.DataFrame(index=mydates,columns=[0,1,2,3,4,5])
    for j in range(0,6):
      for i in range(0, len(mydates)):
        pred_steps.iloc[i][j] = pred[i][j]
    pred_steps[3][0]=last_temp+pred_steps[3][0]
    pred_steps[3]=pred_steps[3].cumsum()
    pred_steps[3]=pred_steps[3].astype(float)
    temperature=pred_steps[3][-1]
  
  except ValueError:
    return "Please check if the values are entered correctly"

  return render_template('index.html',prediction_text="Temperature = {} degree C".format(temperature))

if __name__=="__main__":
  app.run(debug=True,host='0.0.0.0')