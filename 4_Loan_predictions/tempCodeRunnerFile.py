
        x5 = float(data["S_emp"])
        x6 = float(data["ApIn"])
        x7 = float(data["Coap"])
        x8 = float(data["LA"])
        x9 = float(data["LAT"])
        x10 = float(data["CH"])
        x11 = float(data["PA"])

        prd = ut.Predict(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11)

        return "prediction is", prd
    else:
        return"No Predictions"