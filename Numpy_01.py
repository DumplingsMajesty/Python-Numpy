from PIL import Image
import numpy as np

im = np.array(Image.open('../data/lena.jpg'))

print(type(im))
# <class 'numpy.ndarray'>

print(im.dtype)
# uint8

print(im.shape)
# (225, 400, 3)

im_gray = np.array(Image.open('../data/lena.jpg').convert('L'))

print(im_gray.shape)
# (225, 400)

print(im.flags.writeable)
# True

print(im[0, 0, 0])
# 109

im[0, 0, 0] = 0

print(im[0, 0, 0])
# 0

im_as = np.asarray(Image.open('data/src/lena.jpg'))

print(type(im_as))
# <class 'numpy.ndarray'>

print(im_as.flags.writeable)
# False

# im_as[0, 0, 0] = 0
# ValueError: assignment destination is read-only