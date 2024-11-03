import cv2
import numpy as np
from skimage.restoration import denoise_tv_chambolle
import pywt

image = cv2.imread('unsplash.jpg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def display(image, output, output_name):
    cv2.imshow('Original Image', image)
    cv2.imshow(f'{output_name} Image', output)
    cv2.imwrite(f'{output_name}.jpg', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Filtering techniques
gaussian_filtered = cv2.GaussianBlur(image, (9, 9), 0)
display(image, gaussian_filtered, output_name='Gaussian')


bilateral_filtered = cv2.bilateralFilter(image, d=9, sigmaColor=75, sigmaSpace=75)
display(image, bilateral_filtered, output_name='Bilateral')


def retinex(image, sigma_list=[15, 80, 250]):
    image = image.astype(np.float32) + 1.0  # Avoid log(0)
    
    retinex_image = np.zeros_like(image)

    for sigma in sigma_list:
        blurred = cv2.GaussianBlur(image, (0, 0), sigma)
        
        retinex_image += np.log(image) - np.log(blurred)

    retinex_image = retinex_image / len(sigma_list)
    
    retinex_image = cv2.normalize(retinex_image, None, 0, 255, cv2.NORM_MINMAX)
    retinex_image = np.uint8(retinex_image)

    return retinex_image

retinex_result = retinex(image)
display(image, retinex_result, output_name='Retinex')


# Denoising techniques
nlm_denoised = cv2.fastNlMeansDenoising(gray_image, None, h=10, templateWindowSize=7, searchWindowSize=21)
display(image, nlm_denoised, output_name='NLM Denoised')


tv_denoised = denoise_tv_chambolle(image, weight=0.1)
tv_denoised_scaled = (tv_denoised * 255).astype(np.uint8)
display(image, tv_denoised_scaled, output_name='Total Variance Denoised')


b, g, r = cv2.split(image)
def wavelet_denoising(channel):
    coeffs = pywt.wavedec2(channel, 'haar', level=10)
    coeffs_thresholded = list(coeffs)
    
    threshold = 100
    for i in range(1, len(coeffs_thresholded)):
        coeffs_thresholded[i] = tuple(
            pywt.threshold(c, threshold, mode='soft') for c in coeffs_thresholded[i]
        )
    denoised_channel = pywt.waverec2(coeffs_thresholded, 'haar')
    return np.clip(denoised_channel, 0, 255).astype(np.uint8)

denoised_b = wavelet_denoising(b)
denoised_g = wavelet_denoising(g)
denoised_r = wavelet_denoising(r)
denoised_image_combined = cv2.merge((denoised_b, denoised_g, denoised_r))
display(image, denoised_image_combined, output_name='Wavelet Denoising')