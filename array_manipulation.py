import numpy as np

#1d array
a = np.array([1, 2, 3], dtype = 'int16')
c = np.array([1, 2, 3])
#print(a)

#2d array-default int32- and dimensions
b = np.array([[1, 2, 4], [2, 8, 9]])
#print(b.shape)
#print(b)

#get dtype
#print(a.dtype)
#print(b.dtype)

#get size
#print(a.nbytes) #6
#print(c.nbytes) #12

#all zeros array
#print(np.zeros((2, 4)))

#array with any number
#inp = int(input("Number: "))
#print(np.full((2, 5), inp))

#random num matrix
#print(np.random.randint(4, size=(3, 4)))

#prints diaognal of 1
#print(np.identity(5))

#repeat an array down wards
#arr = np.array([[1, 2, 3]])
#n1 = np.repeat(arr, 3, axis = 0)
#print(n1)

#creates this [1 1 1 1 1
#              1 0 0 0 1
#              1 0 9 0 1
#              1 0 0 0 1
#              1 1 1 1 1]
#base = np.ones((5, 5))
#zeros = np.zeros((3, 3))
#zeros[1, 1] = 9
#print(base)#
#print(zeros)
#base[1:4, 1:4] = zeros
#print(base)

#BE CARFEFUL WHEN COPYING -- must use .copy()
a = np.array([1, 2, 3])
b = a
b[0] = 10
print(a)#also [10, 2, 3]
print(b)#[10, 2, 3]