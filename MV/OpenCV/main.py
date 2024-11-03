import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import img_as_uint, img_as_float
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


plt.imsave('ddr_hue.png', ddr_hsv[:,:,0], cmap='hsv')
plt.imsave('ddr_gray.png', ddr_hsv[:,:,1],cmap='gray')
plt.imsave('ddr_value.png', ddr_hsv[:,:,2], cmap='gray')
plt.imsave('ddr_pink_r.png', ddr[:,:,1], cmap='pink_r')
plt.imsave('ddr_pink.png', ddr[:,:,1], cmap='pink')
plt.imsave('ddr_red.png', ddr[:,:,0], cmap='Reds')
plt.imsave('ddr_blue.png', ddr[:,:,1],cmap='Greens')
plt.imsave('ddr_green.png', ddr[:,:,2],cmap='Blues')
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

ddr_hist = cv2.imread('1720934164227801.jpg', cv2.IMREAD_UNCHANGED)
hist, bins = np.histogram(ddr_hist.ravel(), 256, [0,256])
plt.figure(figsize=(8, 6))
plt.hist(ddr_hist.ravel(), 256, [0,256])
plt.title('Histogram of the Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.savefig('histogram.png')
plt.show()

ddr_hist = cv2.imread('1720934164227801.jpg', cv2.IMREAD_UNCHANGED)
if ddr_hist.shape[2] == 4:
    b, g, r, a = cv2.split(ddr_hist)
    channels = [b, g, r, a]
    channel_names = ['Blue', 'Green', 'Red', 'Alpha']
else:
    b, g, r = cv2.split(ddr_hist)
    channels = [b, g, r]
    channel_names = ['Blue', 'Green', 'Red']
plt.figure(figsize=(10, 8))
for i, channel in enumerate(channels):
    hist, bins = np.histogram(channel.ravel(), 256, [0, 256])
    plt.plot(hist, color=channel_names[i].lower(), label=f'{channel_names[i]} Channel')
plt.title('Histogram of the Image Channels')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.legend()
plt.xlim([0, 256])
plt.savefig('histogram_rgba.png')
plt.show()

ddr = cv2.imread('1720934164227801.jpg', cv2.IMREAD_UNCHANGED)
ddr_float = img_as_float(ddr)

# Smoothing Techniques
gaussian_blur = cv2.GaussianBlur(ddr_float, (15, 15), 0)
cv2.imwrite('gaussian.png', (gaussian_blur * 255).astype(np.uint8))

median_blur = cv2.medianBlur(ddr, 15)
cv2.imwrite('median.png', median_blur)

# Sharpening Techniques
laplacian = cv2.Laplacian(ddr_float, cv2.CV_64F)
sharpened_laplacian = cv2.subtract(ddr_float, laplacian)
cv2.imwrite('laplacian.png', (sharpened_laplacian * 255).astype(np.uint8))

blurred = cv2.GaussianBlur(ddr_float, (5, 5), 0)
unsharp_mask = cv2.addWeighted(ddr_float, 1.5, blurred, -0.5, 0)
cv2.imwrite('unsharp.png', (unsharp_mask * 255).astype(np.uint8))

fig, ax = plt.subplots(3, 2, figsize=(12, 12))
ax[0, 0].imshow(ddr_float)
ax[0, 0].set_title('Original Image')
ax[0, 0].axis('off')
ax[0, 1].imshow(gaussian_blur)
ax[0, 1].set_title('Gaussian Blur')
ax[0, 1].axis('off')
ax[1, 0].imshow(median_blur)
ax[1, 0].set_title('Median Blur')
ax[1, 0].axis('off')
ax[1, 1].imshow(sharpened_laplacian)
ax[1, 1].set_title('Sharpened with Laplacian')
ax[1, 1].axis('off')
ax[2, 0].imshow(unsharp_mask)
ax[2, 0].set_title('Unsharp Masking')
ax[2, 0].axis('off')
plt.tight_layout()
plt.show()

image = cv2.imread('1720934164227801.jpg', cv2.IMREAD_UNCHANGED)

# Split the image into BGR channels
b_channel, g_channel, r_channel = cv2.split(image)

# Create images for each channel
# Red channel
red_image = np.zeros_like(image)
red_image[:, :, 2] = r_channel  # Set the red channel

# Green channel
green_image = np.zeros_like(image)
green_image[:, :, 1] = g_channel  # Set the green channel

# Blue channel
blue_image = np.zeros_like(image)
blue_image[:, :, 0] = b_channel  # Set the blue channel

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Save the images
cv2.imwrite('red_channel.png', red_image)
cv2.imwrite('green_channel.png', green_image)
cv2.imwrite('blue_channel.png', blue_image)
cv2.imwrite('grayscale_image.png', gray_image)

# Optional: Display the images to verify
cv2.imshow('Red Channel', red_image)
cv2.imshow('Green Channel', green_image)
cv2.imshow('Blue Channel', blue_image)
cv2.imshow('Grayscale Image', gray_image)