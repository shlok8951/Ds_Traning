import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder,OneHotEncoder

# data = {
#     'color' : ['red','green','blue','orange','green','blue',np.nan]
# }

# df = pd.DataFrame(data)
# # print(df)
# # #df.dropna(df,inplace  = True)
# # df.fillna("colorless",inplace=True)
# # le = LabelEncoder()
# # df["Color_label"] =   le.fit_transform(df)
# # print(df)

# oh = OneHotEncoder()
# df1 = oh.fit_transform(df[[ "color"]])
# print(df1.toarray())

data = {
    'age' : [10,20,np.nan,26,30],
    'gender' : ['male','female','other','male',np.nan],
    'name':['dheeraj','kavi','sapu','yash','hello']
}
df = pd.DataFrame(data)

df['age'] = df['age'].fillna(df['age'].mean(),inplace= True)
df.dropna(axis=0,inplace=True)
print(df)

le = LabelEncoder()
df["gender1"] = le.fit_transform(df["gender"])
print(df)

oe = OneHotEncoder()
df1 = oe.fit_transform(df[["gender"]]).toarray()
print(df1)