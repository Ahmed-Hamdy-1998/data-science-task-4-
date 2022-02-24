a = np.zeros(1, dtype=str)
a[0] = 'hello world'
print(a[0])
# h

##########################
import numpy as np

a = np.empty((10,), dtype='<U4')

b = np.array(['TEST' for _ in range(2)], dtype=str)

print(b)

a[1:3] = b

print(a)
