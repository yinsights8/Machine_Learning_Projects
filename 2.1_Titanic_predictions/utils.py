import pickle
import os
import config

Model_Folder_Path = config.Model_Folder_Path

if not os.path.exists(Model_Folder_Path):
    os.mkdir(Model_Folder_Path)



def predict_cls(Pclass, Gender, Age, SibSp, Parch, Fare, Q, S):

    cls_pred = pickle.load(open(f"{Model_Folder_Path}/model.pkl", "rb"))

    predict = cls_pred.predict([[Pclass, Gender, Age, SibSp, Parch, Fare, Q, S]])
    pred = predict[0]
    print(f"Predictions are:- {pred}")
    return pred


predict_cls(3,0,25,0,1,10,1,0)