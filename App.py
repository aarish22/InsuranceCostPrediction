import pickle
import pandas as pd
import numpy as np
from flask import Flask,request,jsonify,render_template
from sklearn.preprocessing import StandardScaler

app=Flask(__name__)

#import rigde regressor model and standard scaler
ridge_model=pickle.load(open('Models/ridge.pkl','rb'))
standard_scaler=pickle.load(open('Models/scaler (1).pkl','rb'))

## route for home page
@app.route('/')
def index():
    return render_template('index.html')


    
@app.route('/predictdata',methods=['GET','POST'])
def predict_score():
    if request.method=='POST':
        Age=float(request.form.get('Age'))
        Sex=float(request.form.get('Sex'))
        BMI=float(request.form.get('BMI'))
        Children=float(request.form.get('Children'))
        Smoker=float(request.form.get('Smoker'))
        Region=float(request.form.get('Region'))
    else:
        return render_template('Home.html')
    
    new_data_scaled=standard_scaler.transform([[Age,Sex,BMI,Children,Smoker,Region]])
    Result=ridge_model.predict(new_data_scaled)
    
    return render_template('Home.html',Result=round(Result[0],2))
    
if __name__=="__main__":
     app.run(host="0.0.0.0")