import numpy as np

'''numpy.empty()'''
print(np.empty(3))
# [0. 0. 0.]

print(np.empty((2, 3)))
#[[6.46985116e-312 6.46985114e-312 6.46985090e-312]
# [0.00000000e+000 0.00000000e+000 7.41098469e-323]]

print(np.empty(3).dtype)
# float64

print(np.empty(3, dtype=np.int))
# [0 0 0]

print(np.empty(3, dtype=np.int).dtype)
# int32

'''numpy.empty_like()'''
a_int = np.arange(6).reshape((2,3))
print(a_int)
# [[0 1 2]
#  [3 4 5]]

print(np.empty_like(a_int))
# [[76  0  0]
#  [ 0  0  0]]

a_float = np.arange(6).reshape((2,3)) / 10
print(a_float)
# [[ 0.   0.1  0.2]
#  [ 0.3  0.4  0.5]]

print(np.empty_like(a_float))
# [[0.  0.1 0.2]
#  [ [0.3 0.4 0.5]]

print(np.empty_like(a_float, dtype=np.int))
# [[0 1 2]
#  [3 4 5]]