from flask import Flask, request, render_template, jsonify
import pickle
import numpy as np


model = pickle.load(open("model.pkl", "rb"))

app = Flask(__name__)

@app.route("/")
def Home():
    return render_template("index.html")


@app.route("/results", methods=["GET", "POST"])
def predictions():
    data = request.form

    if request.method == "POST":

        x1 = float(data["crim"])
        x2 = float(data["zn"])
        x3 = float(data["indus"])
        x4 = float(data["chas"])
        x5 = float(data["nox"])
        x6 = float(data["rm"])
        x7 = float(data["age"])
        x8 = float(data["dis"])
        x9 = float(data["rad"])
        x10 = float(data["tax"])
        x11 = float(data["ptratio"])
        x12 = float(data["black"])
        x13 = float(data["lstat"])

        
        arr = np.array([[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]])
        res = model.predict(arr)

        return render_template("result.html", result = res[0])
    else:
        return jsonify({"Message": "No Predictions"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)

