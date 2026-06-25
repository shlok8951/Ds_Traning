import numpy as np

#-------------------- Array Fundamental-------------------

arr1 = np.array([10,90,70,40,60,20]) # 1-D Array
print(arr1)

arr2 = np.array([[70,90,10,30,50],[60,80,20,40,100]]) # 2-D Array
print(arr2)

arr3 = np.array([[[1,3,9,5,7],[8,2,6,4,10]],[[30,50,10,70,90],[100,40,60,20,80]]])
print(arr3)

# Array elements can acces by the index
print(arr1[4]) #60
print(arr2[1,3]) #40
print(arr3[1,0,2]) #10

# Arrays is mutable ->can change value in the array by indexes
arr1[3] = 800
print(arr1)


#----------------- Array Attributes ----------------
print(arr1.ndim) #np.ndim(arr1) can be use
print(arr2.ndim) #
print(arr3.ndim) #

print("Elements in 1 D array : " ,arr1.size)
print("Elements in 2 D array : " ,arr2.size)
print("Elements in 3 D array : " ,arr3.size)

print("Shape of 1 D array : ",np.shape(arr1)) # arr1.shape
print("Shape of 2 D array : ",np.shape(arr2)) #(row,col)
print("Shape of 3 D array : ",np.shape(arr3)) #(dim,row,col)

print(arr1.dtype)

#------------------- Array Creatation by Diff Methods --------------

zero_array1 = np.zeros(4) #by default in float64
zero_array2 = np.zeros((3,4),"int64")
zero_array3 = np.zeros((2,3,4))
print(zero_array1)

one_array = np.ones(4)
one_array = np.ones((3,4))
one_array = np.ones((3,2,2),"int64")
print(one_array)

rng_array = np.arange(5) #arange create only one dimantion array 
rng_array = np.arange(4,16,2) # (start,stop,step)

em_array = np.empty(3)
print(em_array)
em_array = np.empty((3,4))
print(em_array)

x = np.full((2,3),7)
print(x)

arr = np.eye(3) #create a 3x3 identity array
print(arr)

random = np.random.random((4,4))
print(random)


ls_array = np.linspace(1,10,6)
print(ls_array.reshape(3,2))


#----------------------- Adding , removingand sorting elements------------

print(np.sort(arr1))
print()
print(np.sort(arr2)) #By default sort each row
print()
print(np.sort(arr3))
print()
print(np.sort(arr1))
print()
print(np.sort(arr2,axis=0)) #By default sort each row
print()
print(np.sort(arr3,axis=1))

a = np.array([[10,20],[30,40]])
b = np.array([[50,60],[20,30]])
print(np.concatenate((a,b),axis=0)) #add as row
print(np.concatenate((a,b),axis=1)) #add as column

# -> Araray can be reshape by using arr.reshap()/ np.reshape(arr,shape=(),order='C)

# ------------------ How to add a new axis to an array --------------
a = np.arange(5)
b = a[np.newaxis,:] #row vectored b = a[:,np.newaxis] #col vectord

#can use np.expand_dims(arr,axis=) for add axis at a specific position


#-------------------- indexing and slicing ----------------

a = np.array([10,20,40,68,98,34,67])
print(a[2:6]) #40-34
print(a[-1:]) #67
print(a[ : -1])#10-67
print(a[3:-1])#68-67
print(a[-1:3])#[]
print(a[-1:-5])#[]
print(a[-1:-5:-1])#67-68
print(a[2:7:2])


b = np.array([[1,2,3,4,5,6],[10,20,30,40,50,60],[100,200,300,400,500,600]])
print(b[0,])
print(b[1:2,])
print(b[2,])
print(b[0:,0])
print(b[0:,1])

print(b[1,2:4]) #30,40
print(b[-1,-1])#600
print(b[1,-1])#60
print(b[-1,0]) #100

print(b[0:,1:])

c = np.array([[[1,2,3],[4,5,6]],[[10,20,30],[40,50,60]]])
# for each rows
print(c[0,0,])
print(c[0,1,])
print(c[1,0,])
print(c[1,1,])

#for each column
print(c[0,0:,0])
print(c[0,0:,1])
print(c[0,0:,2])
print(c[1,0:,0])
print(c[1,0:,1])
print(c[1,0:,2])

print(c[0:,0,])
print(c[0:,1,])

print(c[0:,0:,0])


#--------------------- Filter ----------------------

a = np.array([[10,40,50,20],[60,70,35,89]])
print(np.where(a>20,a,a-10))
print(np.where(a>20,"True", "False"))
print(a[a>35])  # give result in vectored form
print(a[(a>20) & (a<40)])
print((a>40))  #give result in boolean form 
print(np.nonzero(a>35))  # give a tuble which show the indices of true value
b = np.nonzero(a>35)
print(a[b])
print(list(zip(b[0],b[1]))) # generate the coordinates



#-------------------Create a array from existing data------------

a = np.array([[10,20],[30,40]])
b = np.array([[1,2],[3,4]])
print(np.vstack((a,b))) 
print(np.stack((a,b)))  #it convert in 3-D
print(np.hstack((a,b)))

c = np.arange(1,25).reshape(2,12)
print(np.hsplit(c,3))
print(np.hsplit(c,(5,6)))  

c2 = c.copy() #give a deep copy-> allocate new memory for it


#Arrays can perform arithmatic operations +,-,*,/,min,max,sum,mean,prod,std
print(np.sum(a))    #add all elements
print(a.sum(axis=0)) #add corosponding rows
print(a.sum(axis=1)) #add corosponding column


#----------------------------- BroadCasting----------------
#NumPy understands that the multiplication should happen with each cell. 

#------------------------------------------------------

a = np.array([[1,2,3],[4,3,1]])
b = np.ones(3)
print(np.unique(a))
print(np.unique(a,return_index=True))
print(np.unique(a,return_counts=True))


print(a+b)
#x = np.random.default_rng().random((3,2))
x = np.random.default_rng().integers(5,size=(3,2))
print(x)

print(a.transpose())
print(a.T)
print(np.flip(a))

print(a.flatten())
x = a.flatten() #create a new copy give memory for it
x[0]= 5000
print(x)
print(a)
print(a.ravel()) #it give the view /referance
y = a.ravel()
y[3]=1000
print(y)
print(a)

#-----------------------------------Modifier-------------------

arr = np.arange(12).reshape(3,4)
print(arr)
print(np.insert(arr,1,[10,20,30,40],axis=0))  #return a new array
print(np.insert(arr,1,[10,20,30],axis=1))  # return a new array
print(np.insert(arr,1,[10,20,30],axis=None))  # convert in one dimention

print(np.append(arr,[10,20,30,40]))     #add at the end


# ----------------Advance--------------------
a = np.array([10,20,30,40,50])
np.save('ram.npy',a)
b = np.load('ram.npy')
print(b)

np.savetxt('ram2.csv',a)
x = np.loadtxt('ram2.csv')
print(x)


