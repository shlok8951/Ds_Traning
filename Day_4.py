# Function

# def Hello():
#     print("Hello")

# Hello()

# def Hello1(a):
#     print(a)

# Hello1(100)

# def add(a,b):
#     print(a+b)

# add(3,4)

def hi(b ,*a ):
    print(b)
    print(a)
    # print(c)
    # print(d)
    print(type(a))
    print(type(b))

# hi(1,2,3,4,5,6,7,8)    

# def student(a):        # python not support function overloding
#     print(a)

# def student(a,b):
#     print(a,b)    

# student(2)    

def marks(*a):
    for i in a:
        print(i)

#marks(10,20,30,40,50)      

# def sum(a,b):
#     return a+b

# result = sum(10,20)
# print(result)  

def address(a):
    for i in a:
        for j in i:
            print(j)

#address(["Hello","Shlok"])        

def my(*a ,**b):
    for i in a:
        print(i)
    for key,value in b.items():
        print(f"{key} = {value}")    

# my('hi' , 'shlok',first = 'shlok',last = 'Jain')  
p = "Hello shlok"
def f1():
    print(p)
    s = 'I love GeeksforGeeks'
    def f2():
        print(s)
        
    f2()
#f1()      

#Lembda function

sum = lambda x,y : x+y

#print(sum(100,20))

#Lilst Comprehension:

square = [x**2 for x in range(1,6)]
#print(square)

# hi = lambda *x : x
# print(hi(10,20,30)) #give a tuple

# hi2 = lambda x : [print(i) for i in x]
# hi2([10,20,30,40]) #print single single values

# hi3 = lambda *x : [i for i in x]
# print(hi3(10,20,30))  # give a list

# l = [1,2,3,4,5]
# [print(i) for i in l]

li = [10,20,30,40,50,60]
# #[print(i) for i in li[-1]]

[print(li[i]) for i in range(2,len(li))]

# li = [10,20,30,40]
# print(li)
# li.append(50)
# print(li)
# li.insert(1,100) # use for insert a value at a specific position
# print(li)

# l2 = [100,200,300,400]
# li.extend(l2)
# print(li)

# li = [10,30,{"name":"shlok",
#              "Address":['jaipur','kukas','home','friend']}]
# [print(i) for i in li[-1]['Address']]

# li2 = [10,20,30,[40,50,[60,70,80]]]
# for i in range(0,len(li2[3])-1):
#     print(li2[3][i])

d = {'name':'Hello',
     'age': 20
}
print(d['name'])
print(d.keys())
print(d.values())
for i in d.keys():
    print(i ,"=")
    print(d[i])