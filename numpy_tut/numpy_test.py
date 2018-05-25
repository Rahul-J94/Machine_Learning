import numpy as np 
# a = np.array([[1,2,3,4,5,6,7,8,9], [9,8,7,4,5,6,1,2,3]], dtype = np.uint32, ndmin = 2)
# print (a)

# df = np.dtype('i4s')

# print (df)

# a = np.array([[1,2,3], [4,5,6]])
# print (a.shape)
# a.shape = (3,2)
# b = a.reshape(3,2)
# print (a)
# print (b)

# b = np.arange(20)
# c = b.reshape(2,5,2)
# print (c)
# print (c.ndim)
# print (c.itemsize)
# print (c.flags)

# m = np.empty([2,3,4], dtype=int)
# print (m)

# f = np.ones([2,3,4], dtype=int, order= 'F')
# print (f)

# z = np.zeros([5,], dtype=float, order='C')
# print (z)

# k = [(1,2,3,4),(5,6)]
# p = np.asarray(k)
# print (p)

# list = range(5) 
# it = iter(list)  
# x = np.fromiter(it, dtype = float) 
# print (x)

# list = np.arange(5,78,9, dtype = float) # makes a list of integers within start(5) and end value(78) seperated with distance(9)
# print (list)

# p = np.linspace(10,30, 10, endpoint = False,retstep = True) #make array of 10 digits with equal spacing, retstep print the step size used
# print (p)

# p = np.logspace(1.0,2.0, num=10)
# print (p)

# a = np.arange(25)
# s = slice(5,25,3)
# print (a[s])

# a = np.arange(25)
# b = a[1:20:3]
# print (b)

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# m = a[1:]
# print(m)

# a = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print (a)

# print ("o/p items of second column")
# print( a[...,1])

# print("o/p items of second row")
# print( a[1,...])

# print ('The items column 1 onwards are:' )
# print (a[...,1:])

