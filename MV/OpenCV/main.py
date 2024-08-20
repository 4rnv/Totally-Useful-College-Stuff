import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_uint
from skimage.io import imshow, imread
from skimage import io, color
from skimage.color import rgb2hsv
from skimage.color import rgb2gray

array_1 = np.array([[255, 0],[0, 255]])
imshow(array_1, vmin=0, vmax=255)


array_spectrum = np.array([np.arange(0,255,100),np.arange(255,0,-100),np.arange(0,255,100),np.arange(255,0,-100)])
fig, ax =plt.subplots(1, 2,figsize=(8,6))
ax[0].imshow(array_spectrum, cmap= 'gray')
ax[0].set_title('Arange Generation')
ax[1].imshow(array_spectrum.T, cmap= 'gray')
ax[1].set_title('Transpose Generation')
plt.show()

coloured_array = np.array([[190,10,50],[0,0,0]]*10)
coloured_array = coloured_array.reshape(4, 5, 3)
plt.imshow(coloured_array)
plt.axis('off')
plt.show()

ddr = imread('1720934164227801.jpg')
print(ddr.shape)
plt.imshow(ddr)
plt.axis('off')
plt.colorbar()
plt.show()

ddr_hsv = rgb2hsv(ddr)
fig, ax = plt.subplots(1, 3, figsize=(12,4), sharey = True)
ax[0].imshow(ddr_hsv[:,:,0], cmap='hsv')
ax[0].set_title('Hue')
ax[1].imshow(ddr_hsv[:,:,1],cmap='gray')
ax[1].set_title('Saturation')
ax[2].imshow(ddr_hsv[:,:,2], cmap='gray')
ax[2].set_title('Value')
plt.show()

plt.imsave('ddr_pink_r.png', ddr[:,:,1], cmap='pink_r')
plt.imsave('ddr_pink.png', ddr[:,:,1], cmap='pink')
plt.imsave('ddr_purplemania_red.png', ddr[:,:,0], cmap='Purples')
plt.imsave('ddr_purplemania_green.png', ddr[:,:,1], cmap='Purples')
plt.imsave('ddr_purplemania_blue.png', ddr[:,:,2], cmap='Purples')
plt.imsave('ddr_plasma.png', ddr[:,:,1], cmap='plasma')

fig, ax = plt.subplots(3, 3, figsize=(12,8), sharey =True)
ax[0][0].imshow(ddr[:,:,0], cmap='Reds')
ax[0][0].set_title('Red')
ax[0][1].imshow(ddr[:,:,1],cmap='Greens')
ax[0][1].set_title('Green')
ax[0][2].imshow(ddr[:,:,2],cmap='Blues')
ax[0][2].set_title('Blue')
ax[1][0].imshow(ddr[:,:,0], cmap='Accent')
ax[1][0].set_title('Accent')
ax[1][1].imshow(ddr[:,:,1],cmap='Oranges')
ax[1][1].set_title('Orange')
ax[1][2].imshow(ddr[:,:,1],cmap='plasma')
ax[1][2].set_title('Plasma')
ax[2][0].imshow(ddr[:,:,0], cmap='Purples')
ax[2][0].set_title('Purplemania')
ax[2][1].imshow(ddr[:,:,1],cmap='pink_r')
ax[2][1].set_title('Pink R')
ax[2][2].imshow(ddr[:,:,1],cmap='pink')
ax[2][2].set_title('Pink')
plt.show()

ddr_hist = cv2.imread('1720934164227801.jpg', 0)
hist, bins = np.histogram(ddr_hist.ravel(), 256, [0,256])
plt.hist(ddr_hist.ravel(), 256, [0,256])
plt.show()