from flask import Flask, request, render_template, jsonify
import numpy as np
import pandas as pd
import sklearn
import pickle


model = pickle.load(open("Model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("heart.html")

@app.route("/preds", methods=['GET', 'POST'])
def prediction():
    data = request.form

    if request.method == "POST":
        age      = float(data["age"])
        sex      = float(data["sex"])
        cp       = float(data["cp"]) 
        trestbps = float(data["trestbps"])
        chol     = float(data["chol"])
        fbs      = float(data["fbs"])
        restecg  = float(data["restecg"])
        thalach  = float(data["thalach"])
        exang    = float(data["exang"])
        oldpeak  = float(data["oldpeak"]) 
        slope    = float(data["slope"])
        ca       = float(data["ca"]) 
        thal     = float(data["thal"])

        vars = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                         thalach,exang, oldpeak, slope, ca, thal]])

        res = model.predict(vars)
        pred = res[0]
        if pred == 1:
            pred = "the patient is likely to have Heart disease!"
        else:
            pred= "patient does not likely to have heart disease!"

        return render_template("heart.html", result=pred)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=False)
    # app.run(debug=True)