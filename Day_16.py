import pandas as pd

url = "https://raw.githubusercontent.com/rajendra0968jangid/Ds-Arya/main/student-data.json"
df = pd.read_json(url)
print(df)
print(df.sort_values("english")) #by default ascending
print(df.sort_values("english",ascending=False)) # Decending order , By use inplace we can change in df permanent
print(df)
print(df.sort_values(by=["english","maths"],ascending= [True,False]))
print(df.sort_values("name"))
df["name"] = df["name"].str.lower()
print(df.sort_values("name"))

df["Total"] = df["physics"] + df["maths"] + df["english"]
print(df)

df.loc[14] = ["shlok","Male",60,70,50,180]
print(df)


df.drop("Total",axis=1)
df.drop(14,axis=0)
df["doj"] = pd.date_range("20250601",periods=15)
print(df)
# df.drop(6,7,8,9,10,11,13)
print(df["doj"].dt.year)
print(df["doj"].dt.day)
print(df["doj"].dt.month)
print(df["doj"].dt.day_name())
print(df["doj"]+pd.to_timedelta("20 days")) #(20,unit"D")