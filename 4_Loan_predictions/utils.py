import config
import pickle
import os

Model_Folder_Path = config.MODEL_FOLDER_PATH

if not os.path.exists(Model_Folder_Path):
    os.mkdir(Model_Folder_Path)

def Predict(Gen, Mar, Dep, Edu, S_emp, ApIn, Coap, LA, LAT, CH, PA):

    clsfir = pickle.load(open(f"{Model_Folder_Path}/model.pkl", "rb"))

    pred = clsfir.predict([[Gen, Mar, Dep, Edu, S_emp, ApIn, Coap, LA, LAT, CH, PA]])

    predict = pred[0]

    # print("predictions:- ", predict)

    return predict

Predict(1,0,0,0,0,5849,0.0,145.08,360,1,2)