import pickle
import os
import config

MODEL_PATH = config.model_folder_path

if not os.path.exists(MODEL_PATH):
    os.mkdir(MODEL_PATH)

def Predicts(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13):

    Model = pickle.load(open(f"{MODEL_PATH}/model.pkl", "rb"))

    pred = Model.predict([[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]])

    predict = pred[0]
    # print("predictions:- ", predict)
    return predict


# Predicts(88.6, 168.8, 64.1, 48.8, 2548.0, 130.0, 3.47, 2.68, 9.0, 111.0, 5000.0, 21.0, 27.0)