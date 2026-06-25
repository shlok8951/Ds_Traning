import numpy as np

#---------------------Reshape--------------------------
# arr = np.arange(12)
# print(arr)
# arr2 = np.reshape(arr,(3,4))
# print(arr2)
# arr3 = np.reshape(arr,(2,2,3))
# print(arr3)
# arr1 = arr3.flatten() #create a copy
# print(arr1)
# print(arr2.ravel())    # give the view/referance ->by this we can change original data
# print(arr3.ravel())
# print(arr2)
# print(arr3)
#-------------------------Sorting data ------------------------------

# n = np.array([3,2,5,4,7,3,7,1,5,9,8,6])
# print(n)
# print(np.sort(n))

# n2 = np.reshape(n,(4,3))
# print(n2)
# print(np.sort(n2,axis =0))  #rows sort
# print(np.sort(n2,axis =1))  #col sort



#-------------------------------Slicing----------------------

n = np.arange(12)
# print(n)
# print(n[3:7])
# print(n[ :-1])
# print(n[-1:])

a = np.reshape(n,(3,4))
# print(a)
# print(a[0:1,1:3])
# print(a[-1,-1])
# print(a[0:2,])
# print(a[-1,])

# b = np.reshape(n,(2,2,3))
# print(b)
# print(b[1,0,0])
# print(b[1,1,])
# print(b[0:2,1,])

# c = np.arange(24).reshape(3,4,2)
# print(c[0:3:2,0:4:3,])

#------------------------loop-----------------


# x = np.arange(12).reshape(3,4)
# # p = x.shape
# # print(p)
# i=0
# while i<((x.shape)[0]):
#     j=0
#     while j<(x.shape[1]):
#         print(x[i][j],end=" ")
#         j += 1
#     print()
#     i+=1

#for 3D
y = np.arange(12).reshape(2,2,3)
print(len(y))
print(len(y[0]))
print(len(y[0][0]))
# i =0
# while i<y.shape[0]:
#     j=0
#     while j<y.shape[1]:
#         k=0
#         while k<y.shape[2]:
#             print(y[i][j][k],end=" ")
#             k += 1
#         print()
#         j+=1
#     print()   
#     i+=1    