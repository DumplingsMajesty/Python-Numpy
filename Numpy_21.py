'''创建矩阵对象：Python列表，numpy.array（），numpy.matrix()'''
import numpy as np
l_2d = [[0, 1, 2], [3, 4, 5]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

print(type(l_2d))
# <class 'list'>

arr = np.array([[0, 1, 2], [3, 4, 5]])
print(arr)
# [[0 1 2]
#  [3 4 5]]

print(type(arr))
# <class 'numpy.ndarray'>

arr = np.arange(6)
print(arr)
# [0 1 2 3 4 5]

arr = np.arange(6).reshape((2, 3))
print(arr)
# [[0 1 2]
#  [3 4 5]]

mat = np.matrix([[0, 1, 2], [3, 4, 5]])
print(mat)
# [[0 1 2]
#  [3 4 5]]

print(type(mat))
# <class 'numpy.matrix'>

mat = np.matrix(arr)
print(mat)
# [[0 1 2]
#  [3 4 5]]

print(type(mat))
# <class 'numpy.matrix'>

mat_1d = np.matrix([0, 1, 2])
print(mat_1d)
# [[0 1 2]]

print(type(mat_1d))
# <class 'numpy.matrix'>

print(mat_1d.shape)
# (1, 3)

# mat_3d = np.matrix([[[0, 1, 2]]])
# ValueError: matrix must be 2-dimensional


'''获取和更改（分配）矩阵元素'''
print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

print(l_2d[0][1])
# 1

l_2d[0][1] = 100
print(l_2d)
# [[0, 100, 2], [3, 4, 5]]

print(arr)
# [[0 1 2]
#  [3 4 5]]

print(arr[0, 1])
# 1

arr[0, 1] = 100
print(arr)
# [[  0 100   2]
#  [  3   4   5]]

'''转置矩阵：.T属性'''
l_2d = [[0, 1, 2], [3, 4, 5]]
print(l_2d)
# [[0, 1, 2], [3, 4, 5]]

print([list(x) for x in list(zip(*l_2d))])
# [[0, 3], [1, 4], [2, 5]]

arr = np.arange(6).reshape((2, 3))
print(arr)
# [[0 1 2]
#  [3 4 5]]

print(arr.T)
# [[0 3]
#  [1 4]
#  [2 5]]

'''矩阵总和与差：+运算符，-运算符'''
l_2d_1 = [[0, 1, 2], [3, 4, 5]]
l_2d_2 = [[0, 2, 4], [6, 8, 10]]

print(l_2d_1 + l_2d_2)
# [[0, 1, 2], [3, 4, 5], [0, 2, 4], [6, 8, 10]]

# print(l_2d_1 - l_2d_2)
# TypeError: unsupported operand type(s) for -: 'list' and 'list'

arr1 = np.arange(6).reshape((2, 3))
print(arr1)
# [[0 1 2]
#  [3 4 5]]

arr2 = np.arange(0, 12, 2).reshape((2, 3))
print(arr2)
# [[ 0  2  4]
#  [ 6  8 10]]

print(arr1 + arr2)
# [[ 0  3  6]
#  [ 9 12 15]]

print(arr1 - arr2)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

print(mat1 + mat2)
# [[ 0  3  6]
#  [ 9 12 15]]

print(mat1 - mat2)
# [[ 0 -1 -2]
#  [-3 -4 -5]]

'''标量乘法和按元素乘积：*运算符，numpy.multiply（）'''
print(l_2d_1 * 2)
# [[0, 1, 2], [3, 4, 5], [0, 1, 2], [3, 4, 5]]

# print(l_2d_1 * l_2d_2)
# TypeError: can't multiply sequence by non-int of type 'list'

print(arr1 * 2)
# [[ 0  2  4]
#  [ 6  8 10]]

print(mat1 * 2)
# [[ 0  2  4]
#  [ 6  8 10]]

print(np.multiply(arr1, arr2))
# [[ 0  2  8]
#  [18 32 50]]

print(np.multiply(mat1, mat2))
# [[ 0  2  8]
#  [18 32 50]]

print(arr1 * arr2)
# [[ 0  2  8]
#  [18 32 50]]

'''矩阵乘积：numpy.dot（），numpy.matmul（），@运算符，*运算符'''
arr1 = np.arange(4).reshape((2, 2))
print(arr1)
# [[0 1]
#  [2 3]]

arr2 = np.arange(6).reshape((2, 3))
print(arr2)
# [[0 1 2]
#  [3 4 5]]

print(np.dot(arr1, arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(arr1.dot(arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(np.matmul(arr1, arr2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(arr1 @ arr2)
# [[ 3  4  5]
#  [ 9 14 19]]

mat1 = np.matrix(arr1)
mat2 = np.matrix(arr2)

print(np.dot(mat1, mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1.dot(mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(np.matmul(mat1, mat2))
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1 @ mat2)
# [[ 3  4  5]
#  [ 9 14 19]]

print(mat1 * mat2)
# [[ 3  4  5]
#  [ 9 14 19]]

'''求幂：**运算符'''
arr = np.arange(1, 5).reshape(2, 2)
print(arr)
# [[1 2]
#  [3 4]]

print(arr**2)
# [[ 1  4]
#  [ 9 16]]

mat = np.matrix(arr)
print(mat)
# [[1 2]
#  [3 4]]

print(mat**2)
# [[ 7 10]
#  [15 22]]

print(mat**2 == mat * mat)
# [[ True  True]
#  [ True  True]]

print(mat**3 == mat * mat * mat)
# [[ True  True]
#  [ True  True]]

# print(arr**-1)
# ValueError: Integers to negative integer powers are not allowed.

arr_f = np.array(arr, dtype=float)
print(arr_f**-1)
# [[1.         0.5       ]
#  [0.33333333 0.25      ]]

print(mat**-1)
# [[-2.   1. ]
#  [ 1.5 -0.5]]

print(mat**-2)
# [[ 5.5  -2.5 ]
#  [-3.75  1.75]]

print(mat**-2 == mat**-1 * mat**-1)
# [[ True  True]
#  [ True  True]]

print(mat**-3 == mat**-1 * mat**-1 * mat**-1)
# [[ True  True]
#  [ True  True]]

'''矢量点积：numpy.inner（）'''
v = np.array([0, 1, 2])
print(v)
# [0 1 2]

print(v.shape)
# (3,)

print(np.inner(v, v))
# 5

print(type(np.inner(v, v)))
# <class 'numpy.int64'>

print(np.dot(v, v))
# 5

print(np.matmul(v, v))
# 5

print(v @ v)
# 5

arr_row = np.arange(3).reshape(1, 3)
print(arr_row)
# [[0 1 2]]

print(arr_row.shape)
# (1, 3)

arr_col = np.arange(3).reshape(3, 1)
print(arr_col)
# [[0]
#  [1]
#  [2]]

print(arr_col.shape)
# (3, 1)

arr = np.arange(9).reshape(3, 3)
print(arr)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

print(v @ arr)
# [15 18 21]

print(arr_row @ arr)
# [[15 18 21]]

print(arr @ v)
# [ 5 14 23]

print(arr @ arr_col)
# [[ 5]
#  [14]
#  [23]]

'''逆矩阵：numpy.linalg.inv（），**-1，.I属性'''
arr = np.array([[2, 5], [1, 3]])

arr_inv = np.linalg.inv(arr)
print(arr_inv)
# [[ 3. -5.]
#  [-1.  2.]]

mat = np.matrix([[2, 5], [1, 3]])

mat_inv = np.linalg.inv(mat)
print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

mat_inv = mat**-1
print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

mat_inv = mat.I
print(mat_inv)
# [[ 3. -5.]
#  [-1.  2.]]

result = mat * mat.I
print(result)
# [[1. 0.]
#  [0. 1.]]

# print(arr.I)
# AttributeError: 'numpy.ndarray' object has no attribute 'I'

arr_s = np.array([[0, 0], [1, 3]])

# print(np.linalg.inv(arr_s))
# LinAlgError: Singular matrix

arr_pinv = np.linalg.pinv(arr_s)
print(arr_pinv)
# [[0.  0.1]
#  [0.  0.3]]

print(arr_s @ arr_inv)
# [[0. 0.]
#  [0. 1.]]

print(np.linalg.pinv(arr_pinv))
# [[0. 0.]
#  [1. 3.]]

print(np.linalg.inv(arr))
# [[ 3. -5.]
#  [-1.  2.]]

print(np.linalg.pinv(arr))
# [[ 3. -5.]
#  [-1.  2.]]

mat_s = np.mat([[0, 0], [1, 3]])

# print(np.linalg.inv(mat_s))
# LinAlgError: Singular matrix

# print(mat_s**-1)
# LinAlgError: Singular matrix

# print(mat_s.I)
# LinAlgError: Singular matrix

print(np.linalg.pinv(mat_s))
# [[0.  0.1]
#  [0.  0.3]]

'''行列式：numpy.linalg.det（）'''
arr = np.array([[0, 1], [2, 3]])

det = np.linalg.det(arr)
print(det)
# -2.0

'''特征值和特征向量：numpy.linalg.eig（）'''
arr = np.array([[8, 1], [4, 5]])

w, v = np.linalg.eig(arr)

print(w)
# [9. 4.]

print(v)
# [[ 0.70710678 -0.24253563]
#  [ 0.70710678  0.9701425 ]]

print('value: ', w[0])
print('vector: ', v[:, 0] / v[0, 0])
# value:  9.0
# vector:  [1. 1.]

print(w[np.argmax(w)])
print(v[:, np.argmax(w)])
# 9.0
# [0.70710678 0.70710678]

def get_eigenpairs(arr):
    w, v = np.linalg.eig(arr)
    eigenpairs = []

    for i, val in enumerate(w):
        vec = v[:, i] / np.min(np.abs(v[:, i][v[:, i] != 0]))
        eigenpairs.append((val, vec))

    return eigenpairs

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: 9.0, vector: [1. 1.]
# value: 4.0, vector: [-1.  4.]

arr = np.array([[1, 1, 2], [0, 2, -1], [0, 0, 3]])

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: 1.0, vector: [1. 0. 0.]
# value: 2.0, vector: [1. 1. 0.]
# value: 3.0, vector: [ 1. -2.  2.]

arr = np.array([[3, 2], [-2, 3]])

eigenpairs = get_eigenpairs(arr)

for val, vec in eigenpairs:
    print('value: {}, vector: {}'.format(val, vec))
# value: (3+2.0000000000000004j), vector: [0.-1.j 1.+0.j]
# value: (3-2.0000000000000004j), vector: [0.+1.j 1.-0.j]

'''numpy.ndarray和numpy.matrix之间的差异摘要'''

