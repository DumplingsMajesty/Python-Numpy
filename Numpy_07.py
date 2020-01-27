from PIL import Image
import numpy as np


'''np.linspace()'''
print(np.linspace(0, 10, 3))
# [ 0.  5. 10.]

print(np.linspace(0, 10, 4))
# [ 0.          3.33333333  6.66666667 10.        ]

print(np.linspace(0, 10, 5))
# [ 0.   2.5  5.   7.5 10. ]

print(np.linspace(10, 0, 5))
# [10.   7.5  5.   2.5  0. ]

'''np.tile()'''
a = np.array([0, 1, 2, 3])

print(np.tile(a, 2))
# [0 1 2 3 0 1 2 3]

print(np.tile(a, (3, 2)))
# [[0 1 2 3 0 1 2 3]
#  [0 1 2 3 0 1 2 3]
#  [0 1 2 3 0 1 2 3]]

print(np.tile(a, (2, 1)))
# [[0 1 2 3]
#  [0 1 2 3]]

a = np.array([[11, 12], [21, 22]])

print(np.tile(a, 2))
# [[11 12 11 12]
#  [21 22 21 22]]

print(np.tile(a, (3, 2)))
# [[11 12 11 12]
#  [21 22 21 22]
#  [11 12 11 12]
#  [21 22 21 22]
#  [11 12 11 12]
#  [21 22 21 22]]

print(np.tile(a, (2, 1)))
# [[11 12]
#  [21 22]
#  [11 12]
#  [21 22]]

'''渐变图片的生成（代码）'''
def get_gradation_2d(start, stop, width, height, is_horizontal):
    if is_horizontal:
        return np.tile(np.linspace(start, stop, width), (height, 1))
    else:
        return np.tile(np.linspace(start, stop, height), (width, 1)).T

def get_gradation_3d(width, height, start_list, stop_list, is_horizontal_list):
    result = np.zeros((height, width, len(start_list)), dtype=np.float)

    for i, (start, stop, is_horizontal) in enumerate(zip(start_list, stop_list, is_horizontal_list)):
        result[:, :, i] = get_gradation_2d(start, stop, width, height, is_horizontal)

    return result

array = get_gradation_3d(512, 256, (0, 0, 0), (255, 255, 255), (True, True, True))
Image.fromarray(np.uint8(array)).save('../data/blog/pic/07/gradation_h.jpg', quality=95)

array = get_gradation_3d(512, 256, (0, 0, 0), (255, 255, 255), (False, False, False))
Image.fromarray(np.uint8(array)).save('../data/blog/pic/07/gradation_v.jpg', quality=95)

array = get_gradation_3d(512, 256, (0, 0, 192), (255, 255, 64), (True, False, False))
Image.fromarray(np.uint8(array)).save('../data/blog/pic/07/gradation_color.jpg', quality=95)