import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

url = "https://raw.githubusercontent.com/shlok8951/Ds_Traning/main/projectdata.csv"
df = pd.read_csv(url)
print(df.head())
#print(df.isna().sum())

gender_counts = df['Gender'].value_counts()
#print(gender_counts)

# By Using MatplotLib
fig,aux = plt.subplots(2,2)
aux[0][0].scatter(df["Age"],df["Study_Hours"])
aux[0][1].pie(gender_counts,labels = ['Male','Female'],autopct='%1.1f%%')

aux[1][0].bar(df["Stress_Level"],df["Mental_Health_Score"])
aux[1][0].set_xlabel("Stress Level of Students")
aux[1][0].set_ylabel("Mental Health Score of Student")

aux[1][1].hist(df["Avg_Daily_Usage_Hours"])
aux[1][1].set_title("Avg Daily Usage Hours")
plt.show()

# input
X = df[["Age","Avg_Daily_Usage_Hours","Physical_Activity_Hours",'Sleep_Hours_Per_Night']]

#output
y = df['Mental_Health_Score']

#Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)



# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
age = int(input("Enter the age : "))
use = float(input("Enter the Avg value of daily use : "))
pa =  float(input("Enter the hourse of physical Activity : "))
sleep = float(input("Enter the sleeping Hourse : "))
data1 = {
          "Age":[age],
          "Avg_Daily_Usage_Hours":[use],
          "Physical_Activity_Hours":[pa],
          'Sleep_Hours_Per_Night': [sleep]
}
data = pd.DataFrame(data1)
predictions = model.predict(data)

print("The Mental Health of the Person is : ",predictions[0])

# By using Seaborn  

plt.figure(figsize=(8,6))

sns.scatterplot(x=range(len(y_test)), y=y_test, color="blue", label="Actual")
sns.scatterplot(x=range(len(predictions)), y=predictions, color="red", label="Predicted")

plt.xlabel("Sample")
plt.ylabel("Mental Health Score")
plt.title("Actual vs Predicted")
plt.legend()
plt.show()
