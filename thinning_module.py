import cv2
import numpy as np
import glob

def thinning(image_size):
    back = np.zeros(image_size, dtype='uint8')
    images = glob.glob("imagens/*")
    for image in images:
        kernel = cv2.getStructuringElement(cv2.MORPH_CROSS,(3,3))
        thin = 255*np.ones(back.shape).astype(np.uint8)
        while (cv2.countNonZero(image)!=0):
            erode = cv2.erode(image, kernel)
            opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel)
            subset = erode - opening
            thin = cv2.bitwise_or(subset, thin)
            image = erode.copy()
    return image, thin
image_size = 100, 400
image, thin = thinning(image_size)
cv2.imwrite(f'thinned_images/{image}.png', thin)
