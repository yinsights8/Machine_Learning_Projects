from flask import Flask, request, jsonify
import utils as ut

app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to Flask"

@app.route("/predic", methods=["POST"])
def predictions():
    print("Loading...")
    data = request.form

    if request.method == "POST":
        
        x1 = float(data["Gen"])
        x2 = float(data["Mar"])
        x3 = float(data["Dep"])
        x4 = float(data["Edu"])
        x5 = float(data["S_emp"])
        x6 = float(data["ApIn"])
        x7 = float(data["Coap"])
        x8 = float(data["LA"])
        x9 = float(data["LAT"])
        x10 = float(data["CH"])
        x11 = float(data["PA"])

        prd = ut.Predict(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)

        return jsonify({"prediction is": f"{prd}"})
    else:
        return jsonify({"No ": "Predictions"})

if __name__ == "__main__":
    app.run(debug=True)

