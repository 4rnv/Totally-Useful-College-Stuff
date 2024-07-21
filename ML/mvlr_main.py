import pandas as pd
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

df = pd.read_csv("csv/real_estate.csv")
df = df.drop('X6 longitude', axis=1)
df = df.drop('X5 latitude', axis=1)
df = df.drop('No', axis=1)
median_age = df['X2 house age'].median()
print("Median age of house is " + str(median_age))

reg = linear_model.LinearRegression()
reg.fit(df.drop('Y house price of unit area', axis=1).values, df['Y house price of unit area'])
print(df.head())
print("Coefficients for each feature", reg.coef_)
print(reg.intercept_)

print(reg.predict([[2022,100,2,10]]))
print(reg.predict([[2007,10,1,30]]))
print(reg.predict([[2010,100,2,10]]))

fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111, projection='3d')

# Assuming X2 and X3 are the chosen features
ax.scatter(df['X2 house age'], df['X3 distance to the nearest MRT station'], df['Y house price of unit area'])
ax.set_xlabel('House Age (X2)')
ax.set_ylabel('Distance to MRT (X3)')
ax.set_zlabel('House Price')
plt.show()

#https://aegis4048.github.io/mutiple_linear_regression_and_visualization_in_python