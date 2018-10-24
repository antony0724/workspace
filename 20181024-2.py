import numpy as np
a = np.array([[1,2,3,4,5],[6,7,8,9,10]])
b = a[0][0:2]
c = a[0,0:2]
d = a[1,[0,2]]
e = a[1][[0,2]]
print(b)
print(c)
print(d)
print(e)
