# name = "shlok"
# name1 = name
# print(name == name1)
# print(name is name1)

# x = 295
# y = 295
# print(x==y)
# print(x is y)
# print(id(x) , id(y))

# identity operator -> is or is not
# if value b/w(-5 to 256) then same memory provided


# age = int(input("Enter the age : "))
# if age == 18:
#     print("Your ase is 18")
# elif(age >18):
#     print("Your age greater then 18 : ", age)
# else:
#     print("your age is less then 18 : ",age)

# num = int(input("Enter the your marks: "))
# if num>90:
#     print("A grade")
# elif  num>75:
#     print("B grade")
# elif num>60:
#     print("C grade")
# else:
#     print("Fail")           

# l = [1,2,3,4]
# for i in l:
#     print(i)

# n = int(input("Enter a number : "))
# i = 1
# while i<=10:
#     print(n*i)
#     i += 1    

# d ={
#     'name' : "shlok",
#     'age':21,
#     'pno':'123456789'
# }    
# li = list(d.keys())
# i =0
# while i<len(li ):
#     print(d[li[i]])
#     i += 1

# li = [[10],[11,12,13,14,15]]

# for i in range(len(li[1])):
#     print(li[1][i])
# for i in li:
#     for j in i:
#         print(j)     

i =0
while i<=10:
    i += 1
    if(i == 3):
        continue

    print(i)
    