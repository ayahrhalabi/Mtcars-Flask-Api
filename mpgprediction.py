
import pandas as pd
import numpy as np

from sklearn import linear_model

df = pd.read_csv("mtcars.csv")
col_imp = ["cyl","disp","vs"]
x = df[col_imp]
y = df["mpg"]
regr = linear_model.LinearRegression()
regr.fit(x, y)

def mpgpredict(dict_values, col_imp=col_imp, clf=regr):
    x = np.array([float(dict_values[col]) for col in col_imp])
    x = x.reshape(1,-1)
    y_pred = clf.predict(x)[0]

    return y_pred

