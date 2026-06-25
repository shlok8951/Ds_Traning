# d = {
#     'name':'shlok',
#     'age':21,
#     'city':'xyz'
# }
# print(d.keys())   #give a tuple
# d.update({ 'name':'shivasjs', 'chjg':'sws','age':32})
# print(d)
# del d['city']
# print(d)
# del d['chjg']
# print(d)


# d = {
#     'address':{
#         'address1':{'city':'kukas','state':'rajasthan'},
#         'address2':{'city':'gopalpura','state':'jaipur'}
#     }
# }
# print(d)
# print(d['address'])
# for i in d['address']:
#     for j in d['address'][i]:
#         print(d['address'][i][j])

# l = [10,20,30,['hello','hello1','hello32',[True,False]]]

# d = l[-1:-3:-1]
# for i in d:
#     print(i)

# def sqar(x):
#     return x*x

# l = [1,2,3,4,5,6]
# li = list(map(lambda x:x*x,l))
# print(li)

def helo(x):
    return x.upper()

def helo2(x):
    return x.endswith('a')

li = ['Apple','banana','papaya','cat']
l = list(map(helo,li))
l = list(filter(helo2,li))
print(l)

h = 'shlok'
print(h.upper())

# try : 
#     num = 10
#     num2 = 0
#     div = num/num2
# except:
#     print("Hello")
# finally:
#     print("always")
    
#fillter
import functools
def add(x,y):
    return x+y
li = [10,20,30,40,50]
li2 = [10,2,30,40,50]
l = functools.reduce(add,li)
#l = list(functools.reduce(lambda x,y : x+y,li,li2))
print(l)

