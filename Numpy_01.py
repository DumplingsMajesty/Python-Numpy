from PIL import Image
import numpy as np

'''Numpy图片文件的读取方法'''
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

im_as = np.asarray(Image.open('../data/src/lena.jpg'))
print(type(im_as))
# <class 'numpy.ndarray'>

print(im_as.flags.writeable)
# False

# im_as[0, 0, 0] = 0
# ValueError: assignment destination is read-only

im_f = im.astype(np.float64)
print(im_f.dtype)
# float64

im_f = np.array(Image.open('../data/src/lena.jpg'), np.float64)
print(im_f.dtype)
# float64

'''Numpy图片文件的保存方法'''
pil_img = Image.fromarray(im)
print(pil_img.mode)
# RGB

pil_img.save('../data/temp/lena_save_pillow.jpg')

pil_img_gray = Image.fromarray(im_gray)
print(pil_img_gray.mode)
# L

pil_img_gray.save('../data/temp/lena_save_pillow_gray.jpg')
Image.fromarray(im).save('../data/temp/lena_save_pillow.jpg')
Image.fromarray(im_gray).save('../data/temp/lena_save_pillow_gray.jpg')

# pil_img = Image.fromarray(im_f)
# TypeError: Cannot handle this data type

pil_img = Image.fromarray(im_f.astype(np.uint8))
pil_img.save('../data/temp/lena_save_pillow.jpg')

'''像素值的读取和修改'''
from PIL import Image
import numpy as np

im = np.array(Image.open('../data/src/lena.jpg'))

print(im.shape)
# (225, 400, 3)

print(im[100, 150])
# [111  81 109]

print(type(im[100, 150]))
# <class 'numpy.ndarray'>

R, G, B = im[100, 150]
print(R)
# 111
print(G)
# 81
print(B)
# 109

print(im[100, 150, 0])
# 111
print(im[100, 150, 1])
# 81
print(im[100, 150, 2])
# 109

im[100, 150] = (0, 50, 100)
print(im[100, 150])
# [  0  50 100]

im[100, 150, 0] = 150
print(im[100, 150])
# [150  50 100]

'''图片的单色化和拼接'''
from PIL import Image
import numpy as np

im = np.array(Image.open('../data/src/lena_square.png'))

im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
# im_RGB = np.hstack((im_R, im_G, im_B))
# im_RGB = np.c_['1', im_R, im_G, im_B]
pil_img = Image.fromarray(im_RGB)
pil_img.save('../data/dst/lena_numpy_split_color.jpg')

'''像素值的反转'''
import numpy as np
from PIL import Image

im = np.array(Image.open('../data/src/lena_square.png').resize((256, 256)))
im_i = 255 - im
Image.fromarray(im_i).save('../data/dst/lena_numpy_inverse.jpg')

'''减色处理'''
import numpy as np
from PIL import Image

im = np.array(Image.open('../data/src/lena_square.png').resize((256, 256)))
im_32 = im // 32 * 32
im_128 = im // 128 * 128
im_dec = np.concatenate((im, im_32, im_128), axis=1)
Image.fromarray(im_dec).save('../data/dst/lena_numpy_dec_color.png')

'''四则运算'''
from PIL import Image
import numpy as np

im = np.array(Image.open('../data/src/lena_square.png'))
im_1_22 = 255.0 * (im / 255.0)**(1 / 2.2)
im_22 = 255.0 * (im / 255.0)**2.2
im_gamma = np.concatenate((im_1_22, im, im_22), axis=1)

pil_img = Image.fromarray(np.uint8(im_gamma))
pil_img.save('../data/dst/lena_numpy_gamma.jpg')

'''切片修剪'''
from PIL import Image
import numpy as np

im = np.array(Image.open('../data/src/lena_square.png'))
print(im.shape)
# (512, 512, 3)

im_trim1 = im[128:384, 128:384]
print(im_trim1.shape)
# (256, 256, 3)

Image.fromarray(im_trim1).save('../data/dst/lena_numpy_trim.jpg')

def trim(array, x, y, width, height):
    return array[y:y + height, x:x+width]

im_trim2 = trim(im, 128, 192, 256, 128)
print(im_trim2.shape)
# (128, 256, 3)

Image.fromarray(im_trim2).save('../data/dst/lena_numpy_trim2.jpg')
im_trim3 = trim(im, 128, 192, 512, 128)
print(im_trim3.shape)
# (128, 384, 3)

Image.fromarray(im_trim3).save('../data/dst/lena_numpy_trim3.jpg')

'''按切片或函数的拆分'''
from PIL import Image
import numpy as np

im = np.array(Image.open('../data/src/lena_square.png').resize((256, 256)))
print(im.shape)
# (256, 256, 3)

im_0 = im[:, :100]
im_1 = im[:, 100:]
print(im_0.shape)
# (256, 100, 3)
print(im_1.shape)
# (256, 156, 3)

Image.fromarray(im_0).save('../data/dst/lena_numpy_split_0.jpg')
Image.fromarray(im_1).save('../data/dst/lena_numpy_split_1.jpg')
im_0, im_1 = np.hsplit(im, 2)

print(im_0.shape)
# (256, 128, 3)
print(im_1.shape)
# (256, 128, 3)

im_0, im_1, im_2 = np.hsplit(im, [100, 150])
print(im_0.shape)
# (256, 100, 3)
print(im_1.shape)
# (256, 50, 3)
print(im_2.shape)
# (256, 106, 3)

# im_0, im_1, im_2 = np.hsplit(im, 3)
# ValueError: array split does not result in an equal division

im_0, im_1, im_2 = np.array_split(im, 3, axis=1)
print(im_0.shape)
# (256, 86, 3)
print(im_1.shape)
# (256, 85, 3)
print(im_2.shape)
# (256, 85, 3)

'''切片粘贴'''
import numpy as np
from PIL import Image

src = np.array(Image.open('../data/src/lena_square.png').resize((128, 128)))
dst = np.array(Image.open('../data/src/lena_square.png').resize((256, 256))) // 4

dst_copy = dst.copy()
dst_copy[64:128, 128:192] = src[32:96, 32:96]

Image.fromarray(dst_copy).save('../data/dst/lena_numpy_paste.jpg')

dst_copy = dst.copy()
dst_copy[64:192, 64:192] = src

Image.fromarray(dst_copy).save('../data/dst/lena_numpy_paste_all.jpg')