import numpy as np

x = np.array([1,2,3,4,5,6,7,8,9])
x.reshape(3,3)
print(x)


a = np.ones((10, 2))
print(a)
print(a.shape)


a = np.arange(60).reshape((3, 4, 5))
print(a)

a2 = np.reshape(a,(3,20))

print(a2)

