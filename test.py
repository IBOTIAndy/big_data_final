import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_regression
import seaborn as sns

table = pd.read_csv("end_marge.csv")
table2 = table[table["station_n"] != 0]
table2.sort_index()
print(table2)
X = table[["station_n"]]
Y = table["total_sequence"]

#X = table2[["711_n"]]
#Y = table2["station_n"]
plt.scatter(X, Y)
plt.show()

#plt

lm = LinearRegression()
lm.fit(X, Y)

print(lm.intercept_)
print(lm.coef_)
print(f_regression(X, Y)[1])

predictions = lm.predict(X)
plt.scatter(Y, predictions)
#plt.show()
sns.distplot((Y-predictions))
