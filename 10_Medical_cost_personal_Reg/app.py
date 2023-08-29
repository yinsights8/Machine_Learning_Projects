from flask import Flask, request, render_template, jsonify
import pickle
import pandas as pd
import sklearn
import numpy as np

med_data = pd.read_csv("med_insurance.csv")

model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)


@app.route("/")
def Home():
    return render_template("index.html")

@ app.route("/predict", methods=["GET","POST"])
def predictions():
    data = request.form

    if request.method=="POST":
        age = float(data["age"])
        sex = data["sex"]
        bmi = float(data["bmi"])
        children = float(data["children"])
        smoker = data["smoker"]

        predcition = model.predict(pd.DataFrame([[age, sex, bmi, children, smoker]],
                                    columns=["age", "sex", "bmi", "children", "smoker"]))

        res = str(np.around(predcition[0], 3))


    return render_template("index.html", result=res)






if __name__ == "__main__":
    app.run(host="0.0.0.0", port= 8080,debug=False)
    # app.run(debug=True)