import pickle
import config
import os

Model_folder_path = config.Model_Folder

if not os.path.exists(Model_folder_path):
    os.mkdir(Model_folder_path)


def Predictions(al, ma, ash, ala, mag, tp, fl, np, pr, ci, hue, dilwine, pro):

    clasi = pickle.load(open(f"{Model_folder_path}/model.pkl", "rb"))

    model = clasi.predict([[al, ma, ash, ala, mag, tp, fl, np, pr, ci, hue, dilwine, pro]])

    pred = model[0]
    # print(f"Predictions: -{pred}")

    return pred

# Predictions(14.23, 1.71, 2.43, 15.6, 127.0, 2.8, 3.06, 0.28, 2.29, 5.64, 1.04, 3.92, 1065.0)
