import pandas as pd
import numpy as np
# df = pd.read_json("file1.json")
# # print(df)
# # print(df.head(2))
# # print(df.head(-4))  #remove records from botoum 
# # print(df.tail(3))
# # print(df.tail(-4))

# # print(df.shape)
# # print(df.info())
# # print(df.info(verbose=True))  # not hide details
# # print(df.info(verbose=False))
# df["marks"] = [10,20,30,40,50]
# df.rename(columns={"name":"Student_name"} ,inplace=True)
# print(df)

# print(df.describe())

data = {
    "Emp_Id":[101,102,103,104,105,106],
    "Name":["Amit","Riya","raj","Sara","john","Neha"],
    "Department":["IT","HR","Finance","IT","Sales","HR"],
    "Salary":[50000,45000,60000,55000,48000,52000],
    "Experience":[2,3,5,4,1,3]
}
df = pd.DataFrame(data)
print(df)

print(df.head())
print(df.tail())
print(df.info)
print(df.describe())
print(df.rename(columns={"Name":"Emp_Name"},inplace=True))
#rename() (without inplace=True) returns a new DataFrame, and print() displays that returned DataFrame.
#inplace=True, pandas modifies the original DataFrame directly and returns None. The method doesn't create and return a new DataFrame.

