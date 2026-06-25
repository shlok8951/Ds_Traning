import numpy as np

n= np.arange(12)
print(n)
d = n.reshape(4,3)
print(d)
s = d[:,2]
r =d[2,2]
print(s)
w = d[1:3 ,2:3]
print(r)
print(w)