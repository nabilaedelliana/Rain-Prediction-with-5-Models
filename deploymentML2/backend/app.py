from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# initiate model & columns
LABEL = ["Not Rain", "Rain"]
datacol = ['MinTemp', 'Humidity3pm', 'Cloud9am', 'Rainfall', 'WindGustSpeed', 'raintoday','month']

with open("rain_predictor.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def welcome():
    return '<h3>Selamat Datang di Program Backend Saya<h3>'

@app.route("/predict", methods=["GET", "POST"])
def predict_titanic():
    if request.method == "POST":
        content = request.json
        try:
            new_data = {'MinTemp': content['Temperature'],
                        'Humidity3pm': content['Humidity'],
                        'Cloud9am': content['Cloud_Cover'],
                        'Rainfall': content['Rainfall'],
                        'WindGustSpeed': content['Wind_Speed'],
                        'raintoday': content['is_today_rain?'],
                        'month': content['Month']}
            new_data = pd.DataFrame([new_data])
            res = model.predict(new_data)
            result = {'class':str(res[0]),
                      'class_name':LABEL[str(res[0])]}
            response = jsonify(success=True, 
                               result=result)
            return response, 200
        except Exception as e:
            response = jsonify(success=False,
                               message=str(e))
            return response, 400
    
    
    
    return "<p>Silahkan gunakan method POST untuk mode <em>inference model </em></p>"
#app.run(debug=True) # harus dihapus kalo deploy ke heroku