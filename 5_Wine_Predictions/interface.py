from flask import Flask, request, jsonify
import coding as co

app = Flask(__name__)

@app.route("/")
def Welcome():
    return jsonify({"Message": "Welcome to flask"})


@app.route("/predict", methods=["POST"])
def predictions():

    print("Loading...")
    data = request.form

    if request.method == "POST":
        
        x1 = float(data["al"])
        x2 = float(data["ma"])
        x3 = float(data["ash"])
        x4 = float(data["ala"])
        x5 = float(data["mag"])
        x6 = float(data["tp"])
        x7 = float(data["fl"])
        x8 = float(data["np"])
        x9 = float(data["pr"])
        x10 = float(data["ci"])
        x11 = float(data["hue"])
        x12 = float(data["dilwine"])
        x13 = float(data["pro"])
        
        predictor = co.Predictions(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10,x11,x12,x13)

        return jsonify({"Prediction say's": f"{predictor}"})
    else:
        return jsonify({"Unkown":"Predictions"})






if __name__ == "__main__":
    app.run(debug=True)