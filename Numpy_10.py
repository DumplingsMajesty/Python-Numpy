from PIL import Image
import numpy as np

im = np.array(Image.open('./data/10/lena.jpg'))

'''单色化'''
im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)

pil_img_RGB = Image.fromarray(im_RGB)
pil_img_RGB.save('./data/10/lena_numpy_split_color.jpg')

'''黑白化'''
im_gray = 0.299 * im[:, :, 0] + 0.587 * im[:, :, 1] + 0.114 * im[:, :, 2]

print(im.dtype)
print(im_gray.dtype)
# uint8
# float64

print(im.shape)
print(im_gray.shape)
# (512, 512, 3)
# (512, 512)

pil_img_gray = Image.fromarray(np.uint8(im_gray))
pil_img_gray.save('./data/10/lena_numpy_gray.jpg')

'''颜色交换'''
im_swap = im.copy()
im_swap[:, :, 0], im_swap[:, :, 2] = im[:, :, 2], im[:, :, 0]

pil_img_swap = Image.fromarray(im_swap)
pil_img_swap.save('./data/10/lena_numpy_swap_color.jpg')