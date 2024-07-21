import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv("csv/lr.csv")
data = {'X_sum': 0, 'Y_sum': 0, 'XY_sum': 0, 'X2_sum': 0}
print(data)
X = []
Y = []

for index, row in file.iterrows():
    X.append(row['X'])
    Y.append(row['Y'])

count = 0
for index, row in file.iterrows():
    count += 1
    data['X_sum'] += row['X']
    data['Y_sum'] += row['Y']
    data['XY_sum'] += row['X'] * row['Y']
    data['X2_sum'] += row['X']**2
print(data)

a = (count * data['XY_sum'] - data['X_sum'] * data['Y_sum']) / (
    count * data['X2_sum'] - data['X_sum']**2)
b = (1 / count) * (data['Y_sum'] - a * data['X_sum'])

x_vals = []
y_vals = []
for i in range(0, 5):
    num = int(input("Enter num: "))
    x_vals.append(num)
    y_vals.append(a * num + b)
print(a, b)
print(x_vals, y_vals)

plt.plot(x_vals, y_vals)
plt.scatter(X, Y, color="yellow")
plt.xlabel('X')
plt.ylabel('Y')
plt.title("Linear Regression")
plt.show()
