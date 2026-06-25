# class Hello:
#     def __init__(self,name):
#         self.name = name['name']['my']

#     def show(self):
#         print(self.name)    

# h1 = Hello({'name':{'my':'shyam','age':21}})
# h1.show()


class Student:
    def __init__(self , *args):
        self.data = args

    def user(self):
        print("Users :")
        for i in self.data[0]:
            print(i)

    def details(self):
        for i in self.data[1]:
            print(i ,":" ,self.data[1][i])

s1 = Student(["A","B","C","D"],{'add':'kukas','college':'arya','loc':'jaipur'})
s1.user() 
s1.details()       