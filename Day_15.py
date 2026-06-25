import pandas as pd
# d  = {
#     "name":["vishal","ram","shyam","vineet"],
#     "salary":[1000,2200,3000,4000]
# }
# df = pd.DataFrame(d)
# print(df)

# # df["holiday"] = df["salary"]/100
# # df["increment"] = [10,20,30,40]
# # df.drop(["salary","name"],axis=1,inplace=True)
# # print(df)

# print(df.loc[2,"name"])
# print(df.iloc[2,0])

# print(df.loc[1])
# print(df.iloc[1])

# print(df.loc[0:3,["name","salary"]]) #last index include
# print(df.iloc[0:4,0:1]) #last index not include
data = {
    "Emp_Id":[101,102,103,104,105,106],
    "Name":["Amit","Riya","raj","Sara","john","Neha"],
    "Department":["IT","HR","Finance","IT","Sales","HR"],
    "Salary":[50000,45000,60000,55000,48000,52000],
    "Experience":[2,3,5,4,1,3]
}
df = pd.DataFrame(data)
print(df)


print(df[(df["Salary"]>50000) & (df["Experience"]>3)])
print()
print(df.loc[3,["Emp_Id","Salary"]])
print()
print(df.iloc[3,1])

print(df.loc[0:5,["Name","Salary"]])
print(df.iloc[0:4,0:3])
print(df.iloc[0:5:2])

print(df.drop(["Name","Salary"],axis=1))
