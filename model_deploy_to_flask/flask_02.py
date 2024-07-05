from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
import flasgger
from flasgger import Swagger
import os
subfolder = 'model_deploy_to_flask'
original_directory = os.getcwd()
new_directory = os.path.join(original_directory, subfolder)
os.chdir(new_directory)
print(os.getcwd())
app=Flask(__name__)
Swagger(app)
model = os.path.join('..', 'model_training', 'classifier.pkl')
pickle_in = open(model,"rb")
classifier=pickle.load(pickle_in)

@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict',methods=["Get"])
def predict_note_authentication():
    
    """Let's Predict if the test result is abnormal, normal or inconclusive 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Age
        in: query
        type: number
        required: true
      - name: Gender
        in: query
        type: number
        required: true
      - name: Blood Type
        in: query
        type: number
        required: true
      - name: Medical Condition
        in: query
        type: number
        required: true
      - name: Billing Amount
        in: query
        type: number
        required: true
      - name: Billing Amount
        in: query
        type: number
        required: true
      - name: Admission Type
        in: query
        type: number
        required: true
      - name: Medication
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values
        
    """
    age=request.args.get("age")
    gender=request.args.get("gender")
    blood_type=request.args.get("blood_type")
    medical_condition=request.args.get("medical_condition")
    billing_amount=request.args.get("billing_amount")
    admission_type=request.args.get("admission_type")
    medication=request.args.get("medication")

    prediction=classifier.predict([[age,gender,blood_type,medical_condition,billing_amount,admission_type,medication]])
    print(prediction)
    return "Hello The answer is"+str(prediction)

@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    """Let's Predict if the test result is abnormal, normal or inconclusive
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: The output values
        
    """
    df_test=pd.read_csv(request.files.get("file"))
    print(df_test.head())
    prediction=classifier.predict(df_test)
    
    return str(list(prediction))

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000)