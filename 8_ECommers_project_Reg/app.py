from flask import Flask, request, jsonify, render_template
import numpy as np
import sklearn
import pandas as pd
import pickle


app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def wellcome():
    return render_template("index.html")

@app.route("/predict",methods=["GET", "POST"])
def preds():
    data = request.form

    if request.method == "POST":
        av = float(data["av"])
        avglen = float(data["avglen"])
        ToApp = float(data["ToApp"])
        ToWeb = float(data["ToWeb"]) 
        LenMem = float(data["LenMem"])


        inputs = np.array([[av, avglen, ToApp, ToWeb, LenMem]])
        res = model.predict(inputs)

        return render_template("result.html", result=np.around(res[0],3))
    else:
        return jsonify({"Message":"No Predictions"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080,debug=False)
    # app.run(debug=True)