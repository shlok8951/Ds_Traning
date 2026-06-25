from queue import Full

import pandas as pd
import numpy as np
df = pd.read_json("file1.json")
print(df)
df["mark"] = [10,20,30,40,50]
print(df)
# df["mark"]= [10,20,30,40,np.nan]
# print(df)

# df.iloc[4,2] = np.nan
# print(df)

df.loc[4,"mark"] = None
df.loc[3,"roll no"] = None
print(df)

# df.dropna(axis=0,inplace=True)  #drop the complete row
# print(df)

# df.dropna(axis=1,inplace=True)  #derp the column
# print(df)

# df.fillna(df["mark"].mean(),inplace=True)
# print(df)
# df.fillna({"mark": 100,"roll no":200},inplace = True)
# print(df)

df["mark"] = df["mark"].fillna(df["mark"].mean(),inplace=True)
df["roll no"] = df["roll no"].fillna(200,inplace=True)
print(df)

print(df["mark"].agg(["mean","sum","min","max"]))

df1 = df
x = (pd.concat([df,df1],axis=1) )
x.iloc[2,3] = "shlok"
print(x)
