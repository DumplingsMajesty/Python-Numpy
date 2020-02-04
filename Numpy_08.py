import numpy as np

'''numpy.zeros(): 初始化值为0'''
print(np.zeros(3))
# [ 0.  0.  0.]

print(np.zeros((2, 3)))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

print(np.zeros(3).dtype)
# float64

print(np.zeros(3, dtype=np.int))
# [0 0 0]

print(np.zeros(3, dtype=np.int).dtype)
# int64

'''numpy.ones(): 初始化值为1'''
print(np.ones(3))
# [ 1.  1.  1.]

print(np.ones((2, 3)))
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

print(np.ones(3).dtype)
# float64

print(np.ones(3, dtype=np.int))
# [1 1 1]

print(np.ones(3, dtype=np.int).dtype)
# int64

'''numpy.full(): 任意值的初始化'''
print(np.full(3, 100))
# [100 100 100]

print(np.full(3, np.pi))
# [ 3.14159265  3.14159265  3.14159265]

print(np.full((2, 3), 100))
# [[100 100 100]
#  [100 100 100]]

print(np.full((2, 3), np.pi))
# [[ 3.14159265  3.14159265  3.14159265]
#  [ 3.14159265  3.14159265  3.14159265]]

print(np.full(3, 100).dtype)
# int64

print(np.full(3, 100.0).dtype)
# float64

print(np.full(3, np.pi).dtype)
# float64

print(np.full(3, 100, dtype=float))
# [ 100.  100.  100.]

print(np.full(3, np.pi, dtype=int))
# [3 3 3]

'''numpy.zeros_like(): 初始化值为0'''
a_int = np.arange(6).reshape((2,3))
print(a_int)
# [[0 1 2]
#  [3 4 5]]

a_float = np.arange(6).reshape((2,3)) / 10
print(a_float)
# [[ 0.   0.1  0.2]
#  [ 0.3  0.4  0.5]]

print(np.zeros_like(a_int))
# [[0 0 0]
#  [0 0 0]]

print(np.zeros_like(a_float))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

print(np.zeros_like(a_int, dtype=np.float))
# [[ 0.  0.  0.]
#  [ 0.  0.  0.]]

'''numpy.ones_like(): 初始化值为1'''
print(np.ones_like(a_int))
# [[1 1 1]
#  [1 1 1]]

print(np.ones_like(a_float))
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

print(np.ones_like(a_int, dtype=np.float))
# [[ 1.  1.  1.]
#  [ 1.  1.  1.]]

'''numpy.full_like(): 任意值的初始化'''
print(np.full_like(a_int, 100))
# [[100 100 100]
#  [100 100 100]]

print(np.full_like(a_float, 100))
# [[ 100.  100.  100.]
#  [ 100.  100.  100.]]

print(np.full_like(a_int, 0.123))
# [[0 0 0]
#  [0 0 0]]

print(np.full_like(a_float, 0.123))
# [[ 0.123  0.123  0.123]
#  [ 0.123  0.123  0.123]]

print(np.full_like(a_int, 0.123, dtype=np.float))
# [[ 0.123  0.123  0.123]
#  [ 0.123  0.123  0.123]]