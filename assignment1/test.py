import numpy as np
a = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
b = np.array([[0, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [1, 2, 3, 4], [0, 2, 3, 4], [5, 6, 7, 8], [1, 2, 3, 4], [1, 2, 3, 4]])
b = np.split(b, 4)
print(b)
c = np.concatenate(b[:2 ] + b[4: ])
d = b[2]
print(c)
print(d)
print(c[:0])