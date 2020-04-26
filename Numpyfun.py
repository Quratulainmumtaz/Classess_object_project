import numpy as np
x = np.zeros((4 , 4))
print(x)
q=np.ones((5 , 5))
print(q)
l = [1 , 2, 3, 4]
s = np.array(l)
print(s)
r = np.arange(1,100,10)
print(r)
a = np.random.randn((10))
print(a)
b = np.random.randn((10))
print(b)
print(a + b)
print(a - b)
print(2 * a)
print(a > 0)
print(a[a > 0])
x = np.array([1 , 4, 7 ,8 ,9])
print(x[4])
print(x[x > 5])
print(x[[2 , 1]])
z = np.random.randn(10 , 10)
print(z)
print(z[0])
print(z[0][4])
print(z[1:10:2])
print(z[::,0:4])




