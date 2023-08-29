import config
import os
import pickle

path = "model"

if not os.path.exists(path):
    os.mkdir(path)


def predc(isd, bilm, bidm, fpl, bmg, sx):

    cls_mod = pickle.load(open(f"{path}/model.pkl", 'rb'))

    pred = cls_mod.predict([[isd, bilm, bidm, fpl, bmg, sx]])
    p = pred[0]
    
    if p == 0:
        p = "Adelie"
    elif p == 1:
        p = "Chinstrap"
    else:
        p = "Gentoo"

    # print(f"Predictions :- {p}")

    return p

# predc(1, 50, 61, 18, 27, 1)