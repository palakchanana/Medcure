import csv
from flask import Flask, render_template,request,redirect,url_for
import diseaseprediction


app = Flask(__name__)

with open('templates/Testing.csv', newline='') as f:
        reader = csv.reader(f)
        symptoms = next(reader)
        symptoms = symptoms[:len(symptoms)-1]
@app.route('/', methods=['GET'])
def dropdown():
        return render_template('includes/default.html', symptoms=symptoms)

@app.route('/disease_predict', methods=['POST'])
def disease_predict():
    selected_symptoms = []
    if(request.form['First Symptom']!="") and (request.form['First Symptom'] not in selected_symptoms):
        selected_symptoms.append(request.form['First Symptom'])
    if(request.form['Second Symptom']!="") and (request.form['Second Symptom'] not in selected_symptoms):
        selected_symptoms.append(request.form['Second Symptom'])
    if(request.form['Third Symptom']!="") and (request.form['Third Symptom'] not in selected_symptoms):
        selected_symptoms.append(request.form['Third Symptom'])
    if(request.form['Fourth Symptom']!="") and (request.form['Fourth Symptom'] not in selected_symptoms):
        selected_symptoms.append(request.form['Fourth Symptom'])
    if(request.form['Fifth Symptom']!="") and (request.form['Fifth Symptom'] not in selected_symptoms):
        selected_symptoms.append(request.form['Fifth Symptom'])

     disease = diseaseprediction.dosomething(selected_symptoms)
    return render_template('disease_predict.html',disease=disease,symptoms=symptoms)


 
@app.route('/find_doctor', methods=['POST'])
def get_location():
    location = request.form['doctor']
    return render_template('find_doctor.html',location=location,symptoms=symptoms)

@app.route('/drug', methods=['POST'])
def drugs():
    medicine = request.form['medicine']
    return render_template('homepage.html',medicine=medicine,symptoms=symptoms)

if __name__ == '__main__':
    app.run(debug=True)