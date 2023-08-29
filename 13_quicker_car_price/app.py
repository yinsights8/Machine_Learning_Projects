from flask import Flask, render_template, jsonify, request
import pickle
import numpy as np
import pandas as pd

car_data = pd.read_csv("Cleaned_quicker_price.csv")

model = pickle.load(open("lr_model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def Home():

    companies = sorted(car_data["company"].unique())
    car_models = sorted(car_data["name"].unique())
    year = sorted(car_data["year"].unique(), reverse=True)    
    fuel_type = sorted(car_data["fuel_type"].unique())

    return render_template("index.html", companies=companies, car_models=car_models, years=year, fuel_types=fuel_type)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    if request.method == "POST":

        company    = data["company"]
        car_model  = data["car_models"]
        year       = int(data["year"])
        fuel_type  = data["fuel_type"]
        kms_driven = int(data["kilo_driven"])
        # print(company, car_model, year, fuel_type, kms_driven)

        predcition = model.predict(pd.DataFrame([[car_model, company, year, kms_driven, fuel_type]],
        columns=["name", "company", "year", "kms_driven", "fuel_type"]))
        # print(predcition)

        return str(np.around(predcition[0], 3))



if __name__=="__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
