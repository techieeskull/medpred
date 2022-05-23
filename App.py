# -*- coding: utf-8 -*-
"""
Created on Thu May 19 21:37:24 2022

@author: Akash Jadhav
"""

from flask import Flask, render_template, request
import pickle
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('prediction_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        patient_age=int(request.form["Patient_age"])
        patient_gender=request.form["gender"]
        if(patient_gender=="Male"):
            patient_gender=0
        else:
            patient_gender=1
        name_test=request.form["med_test"]
        if(name_test=="Complete Urinalysis"):
            name_test=2
        elif(name_test=="CBC"):
            name_test=1
        elif(name_test=="Acute kidney profile"):
            name_test=0
        elif(name_test=="Fasting blood sugar"):
            name_test=3
        elif(name_test=="TSH"):
            name_test=8
        elif(name_test=="RTPCR"):
            name_test=7
        elif(name_test=="Vitamin D-25Hydroxy"):
            name_test=9
        elif(name_test=="H1N1"):
            name_test=4
        elif(name_test=="Lipid Profile"):
            name_test=6
        elif(name_test=="HbA1c"):
            name_test=5
        type_of_sample=request.form["sample_type"]
        if(type_of_sample=="Blood"):
            type_of_sample=0
        elif(type_of_sample=="Swab"):
            type_of_sample=1
        else:
            type_of_sample=2
        
        way_of_storage=request.form["storage_sample"]
        
        if(way_of_storage=="Normal"):
            way_of_storage=1
        else:
            way_of_storage=0
        
        test_booking_time=float(request.form["test_booking_time"])
        
        cut_off_schedule=request.form["cut_off_schedule"]
        if(cut_off_schedule=="Sample by 5pm"):
            cut_off_schedule=1
        else:
            cut_off_schedule=0
        cut_off_time=float(request.form["cut_off_time"])
        
        Traffic_condition=request.form["Traffic_conditions"]
        if(Traffic_condition=="Medium Traffic"):
            Traffic_condition=2
        elif(Traffic_condition=="Low Traffic"):
            Traffic_condition=1
        else:
            Traffic_condition=0
        time_to_reach_patient=int(request.form["time_to_reach_patient"])
            
        sample_collection_time=int(request.form["sample_collection_time"])
        
        time_to_reach_lab=int(request.form["time_to_reach_lab"])
        
        prediction=model.predict([[patient_age,patient_gender,name_test,type_of_sample,way_of_storage,test_booking_time,cut_off_schedule,cut_off_time,Traffic_condition,time_to_reach_patient,sample_collection_time,time_to_reach_lab]])
        output=prediction[0]
        
        if output=="Y":
            return render_template('index.html',prediction_text="Yes Sample Will Reach On time")
        else:
            return render_template('index.html',prediction_text="Your sample Will Not reach On time")
        
    else:
        return render_template('index.html')
    
    
if __name__=="__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    