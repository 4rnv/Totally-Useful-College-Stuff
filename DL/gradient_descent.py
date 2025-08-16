import numpy as np
import pandas as pd

def mean_square_error(data: pd.DataFrame):
    data["se"] = (data["Y"] - data["Y_pred"]) ** 2
    return data["se"].mean()

def y_(m: float,c: float, data: pd.DataFrame):
    data["Y_pred"] = m * data["X"] + c
    return data

def gradient_of_cost(data: pd.DataFrame):
    data["ke"] = (data["Y"] - data["Y_pred"]) * data["X"]
    return (data["se"].mean())*(-2), (data["ke"].mean())*(-2)

def gradient_descent(old, gradient_of_cost, learning_rate = 0.1):
    new = old - learning_rate * gradient_of_cost
    return new

# data = {
#     "X": [3,5,8,11,12],
#     "Y": [4,6,8,10,14]
# }

data = {
    "X": [1,2,3],
    "Y": [2,2.8,3.6]
}

learning_rate = 0.1
c = 0.5
m = 0.5

df = pd.DataFrame(data)
print(df)

df_pred = y_(m, c, df)
print(df_pred)
mse = mean_square_error(df_pred)

print("MSE: ", mse)
for i in range(10):
    goc_c, goc_m = gradient_of_cost(df_pred)
    print("Gradient of cost m and c: ", goc_m, goc_c)

    m = gradient_descent(m, goc_m, learning_rate)
    c = gradient_descent(c, goc_c, learning_rate)

    print("New m: ", m, "New c: ", c)
        
    df_pred = y_(m, c, df)
    print(df_pred)
    mse = mean_square_error(df_pred)
    print(mse)