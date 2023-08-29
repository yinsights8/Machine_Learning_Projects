from flask import Flask, request, jsonify
import codding as co


app = Flask(__name__)

@app.route('/')
def welcome():
    return "welcome to Flask"

@app.route('/predic',methods=["POST"])
def predictions():
    data = request.form

    if request.method == "POST":

        a = float(data["isd"])
        b = float(data["bilm"])
        c = float(data["bidm"])
        d = float(data["fpl"])
        e = float(data["bmg"])
        f = float(data["sx"])

        pred = co.predc(a,b,c,d,e,f)

        return jsonify({"Prediction": f"{pred}"})
    else:
        return jsonify({"Predcition": "Unknown"})



if __name__ == "__main__":
    app.run(debug=True)