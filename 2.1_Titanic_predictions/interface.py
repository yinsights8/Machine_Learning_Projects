from flask import Flask, jsonify, request
import utils as ut

app = Flask(__name__)

@app.route("/")
def Basic():
    print(f"In flask")
    return jsonify({"Message": "Hello Titanic"})

@app.route("/predict", methods=["POST"])
def predictions():
    print("Loading...")
    data = request.form

    if request.method == "POST":
        x1 = float(data["Pclass"])
        x2 = float(data["Gender"])
        x3 = float(data["Age"])
        x4 = float(data["SibSp"])
        x5 = float(data["Parch"])
        x6 = float(data["Fare"])
        x7 = float(data["Q"])
        x8 = float(data["S"])

        preds = ut.predict_cls(x1,x2,x3,x4,x5,x6,x7,x8)

        return jsonify({"Prediction is" : f"{preds}"})
    else:
        return jsonify({"Prediction is" : "NO"})





if __name__ == "__main__":
    app.run()

