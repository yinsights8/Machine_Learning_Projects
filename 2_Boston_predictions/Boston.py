import pandas as pd
import numpy as np
import pickle
 
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("Boston_df.csv")

X = data.drop(["Unnamed: 0", "medv"], axis=1)
y = data['medv']

print(X)

X_train, x_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=1)

lr_model = LinearRegression()

lr_model.fit(X_train, y_train)


pickle.dump(lr_model, open("model.pkl", "wb"))