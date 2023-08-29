from flask import Flask, request, jsonify
import utils as ut


app = Flask(__name__)

@app.route("/")
def Welcome():
    return "Welcome to the predictions"

@app.route("/predictions",methods=["POST"])
def predictions():
    print("Loading Predictions....")
    data = request.form

    if request.method == "POST":

        a = float(data["x1"])
        b = float(data["x2"])
        c = float(data["x3"])
        d = float(data["x4"])
        e = float(data["x5"])
        f = float(data["x6"])
        g = float(data["x7"])
        h = float(data["x8"])
        i = float(data["x9"])
        j = float(data["x10"])
        k = float(data["x11"])
        l = float(data["x12"])
        m = float(data["x13"])

        pred = ut.Predicts(a,b,c,d,e,f,g,h,i,j,k,l,m)

        return f"Prediction Price is :- {pred}"
    else:
        return "Unkown"

if __name__ == "__main__":
    app.run(debug=True)
