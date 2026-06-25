'''from sklearn.preprocessing import StandardScaler
import pandas as pd
import matplotlib.pyplot as plt
# df = pd.read_csv("data-.csv")
# scaler = StandardScaler()
# df["new"] = scaler.fit_transform(df[["sales"]])
# print(df)

data = {
    'experience':[300,600,900,1500],
    'salary':[1000,1500,2000,3000]
}
df = pd.DataFrame(data)
scaler = StandardScaler()
df["experience"] = scaler.fit_transform(df[[ "experience"]])
df["check"] = scaler.inverse_transform(df[[ "experience"]])
print(df)


# split data exp-> x | sal -> y
X = df['experience'] # capital X
y = df['salary']
 
print(X)
print(y)

plt.plot(X,y)
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("Prediction of Salary according to experience ")
plt.show()

'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# data = {
#     'experience':[300,600,900,1500,2000],
#     'salary':[1000,1500,2000,3000,5000]
# }
url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/extended_salary_data.csv"
df = pd.read_csv(url)
#print(df.head())

X = df[['experience']]
y = df['salary']

x_train, x_test , y_train , y_test  = train_test_split(X,y,test_size=0.2,random_state=2)
# print("x_train : " , x_train)
# print("x_test : ",x_test)
# print("y_train : " , y_train)
# print("y_test : ",y_test)

# Simple Linear Regression

#model fit
model = LinearRegression()
model.fit([x_train,y_train])

user = int(input("Enter experince in days : "))
new_data = {
    'experience':[user]
}

df1 = pd.DataFrame(new_data)
print(df1)
predict_data = model.predict(df1)
print(predict_data[0])


