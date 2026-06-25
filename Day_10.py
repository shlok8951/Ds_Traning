import numpy as np
import math

l = [10,20,30,40]
print(l*2)
# p = l[0:2]  #slicing in list create new list
# print(p)
# p[0] = 100
# print(p)
# print(l)

arr = np.array(l)  #mutable-can be change index value
print(arr*2)
# print(arr)
# x = arr[0:2]  # array slicing give the view / referance of original array

# print(x)
# x[0] = 1000
# print(x)
# # arr[2] = 300
# print(arr)
l = [[1,2,3],[4,5,6]]
# print(l)
arr  = np.array(l)
print(arr.shape)  # give the dimentions in tuple
# print(arr)
# l[1][0] = 100
# arr[1,0]= 100
# print(l)
# print(arr)
# print(arr.ndim)  #2, give the dimantions of the array 
# ar = np.zeros((2,3),dtype="int64")+6
# print(ar)
# p = np.full((2,3),1)
# print(p)

# arr = np.ones((2,3),dtype="int64")
# print(arr*5)

# arr = np.empty((2,3))
# print(arr)

# a = np.linspace(0,10,5,dtype="int64")
# print(a)
# x = np.random.random(5)
# print(x)

# y = np.random.random((2,3))
# print(y)

# z = np.arange(6)
# print(z)

# w = np.arange(12).reshape(3,4)
# print(w)

n =np.array([20,40,10,30,60,90,80])
print(n)
print(np.sort(n))
print(n)
