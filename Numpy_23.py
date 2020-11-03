'''列表 - list'''
l = ['apple', 100, 0.123]
print(l)
# ['apple', 100, 0.123]

l_2d = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

print(l[1])
# 100

print(l_2d[1])
# [3, 4, 5]

print(l_2d[1][1])
# 4

print(l[:2])
# ['apple', 100]

l_num = [0, 10, 20, 30]

print(min(l_num))
# 0

print(max(l_num))
# 30

print(sum(l_num))
# 60

print(sum(l_num) / len(l_num))
# 15.0

l_str = ['apple', 'orange', 'banana']

for s in l_str:
    print(s)
# apple
# orange
# banana

'''数组 - array'''
import array

arr_int = array.array('i', [0, 1, 2])
print(arr_int)
# array('i', [0, 1, 2])

arr_float = array.array('f', [0.0, 0.1, 0.2])
print(arr_float)
# array('f', [0.0, 0.10000000149011612, 0.20000000298023224])

# arr_int = array.array('i', [0, 0.1, 2])
# TypeError: integer argument expected, got float

print(arr_int[1])
# 1

print(sum(arr_int))
# 3
'''多维数组 - numpy.ndarray'''
import numpy as np

arr = np.array([0, 1, 2])
print(arr)
# [0 1 2]

arr_2d = np.array([[0, 1, 2], [3, 4, 5]])
print(arr_2d)
# [[0 1 2]
#  [3 4 5]]

print(arr[1])
# 1

print(arr_2d[1, 1])
# 4

print(arr_2d[0, 1:])
# [1 2]

print(np.sqrt(arr_2d))
# [[0.         1.         1.41421356]
#  [1.73205081 2.         2.23606798]]

arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[1, 2, 3], [4, 5, 6]])

print(np.dot(arr_1, arr_2))
# [[ 9 12 15]
#  [19 26 33]]