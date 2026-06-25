# class Hello:
#     # def __init__(self,name):
#     #     self.name = name

#     def setname(self, name):
#         self.name = name

#     def getname(self):
#         print("The name is : ",self.name)

# h1 = Hello()
# h1.setname("ram")
# h1.getname()    

# class Address:

#     def __init__(city,state):
#         state = state
#         city = city
        

# a1 = Address("rajasthan")
# print(a1.state)

#-------------------- Inheritance -----------------------------

# class addres:
#     def __init__(self,city,state):
#         print("I am parent class")
#         self.city = city
#         self.state = state

#     def display(self):
#         return f"my add. is {self.city} in {self.state}"
    
# class USer(addres):
#     def __init__(self , city,state,name,age):
#         print("hello")
#         super().__init__(city,state)
#         # self.city = city
#         # self.state = state
#         print("i am child class")
#         self.name = name
#         self.age = age

#     def show(self):
#         return f"my name is {self.name},and my age is {self.age}"        


# u1 = USer( "kota","rajasthan", "shlok",21)
# q = u1.show()
# print(q)
# r = u1.display()
# print(r)
# d1 = addres("jaipur","rajasthan")
# p = d1.display()       
# print(p)


#------------------------------- Encapsulation----------------------------

# class Hello:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age  #private attribute

#     def getage(self):
#         return self.__age    


# s1 = Hello("rahhul" , 34)
# p = s1.getage()
# print(p)
# print(s1.__age)


#------------------------Polymorphisam----------------------

class Hello2:
    def __init__(self,city,state):
        self.city = city
        self.state = state

    def show(self):
        print("This is a parent class")

    # def show(self,a,b):
    #     print(a+b)    

class Hello3(Hello2):
    def __init__(self,dis,area):
        self.dis = dis
        self.area = area

    def show(self):
        print("Hello this is a child class")    

H2 = Hello2("Tonk","Rajasthan")
h3 = Hello3("jaipur","toda")
h3.show()
Hello2.show(h3)


#------------------------------------Class Variable---------------------------------------

class A:
    total = 0
    def __init__(self,a,b):
        self.a = a 
        self.b = b
        A.total += 1

    def show(self):
        print(self.total)    
        
a = A(10,10)
a.show()        

b = A(10,29)
b.show()