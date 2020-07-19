'''全体ndarray中满足条件的元素数的计算'''
import numpy as np

a = np.arange(12).reshape((3, 4))
print(a)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

print(a < 4)
# [[ True  True  True  True]
#  [False False False False]
#  [False False False False]]

print(a % 2 == 1)
# [[False  True False  True]
#  [False  True False  True]
#  [False  True False  True]]

print(np.count_nonzero(a < 4))
# 4

print(np.count_nonzero(a % 2 == 1))
# 6

print(np.sum(a < 4))
# 4

print(np.sum(a % 2 == 1))
# 6

'''计算ndarray的每一行和每一列满足条件的元素数'''
print(np.count_nonzero(a < 4, axis=0))
# [1 1 1 1]

print(np.count_nonzero(a < 4, axis=1))
# [4 0 0]

print(np.count_nonzero(a % 2 == 1, axis=0))
# [0 3 0 3]

print(np.count_nonzero(a % 2 == 1, axis=1))
# [2 2 2]

'''使用numpy.any（）（全体，行/列）检查是否有满足条件的元素'''
print(np.any(a < 4))
# True

print(np.any(a > 100))
# False

print(np.any(a < 4, axis=0))
# [ True  True  True  True]

print(np.any(a < 4, axis=1))
# [ True False False]

'''使用numpy.all（）检查所有元素是否都满足条件（全体，行/列）'''
print(np.all(a < 4))
# False

print(np.all(a < 100))
# True

print(np.all(a < 4, axis=0))
# [False False False False]

print(np.all(a < 4, axis=1))
# [ True False False]

'''多种条件'''
print((a < 4) | (a % 2 == 1))
# [[ True  True  True  True]
#  [False  True False  True]
#  [False  True False  True]]

print(np.count_nonzero((a < 4) | (a % 2 == 1)))
# 8

print(np.count_nonzero((a < 4) | (a % 2 == 1), axis=0))
# [1 3 1 3]

print(np.count_nonzero((a < 4) | (a % 2 == 1), axis=1))
# [4 2 2]