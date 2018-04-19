import cv2
import numpy as np 
import matplotlib.pyplot as plt 

#0 = IMREAD_GRAYSCALE
img = cv2.imread('GEE_test', cv2.IMREAD_GRAYSCALE)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# plt.imshow(img, cmap='gray', interpolation='bicubic')
# plt.show()

cv2.imwrite('/home/colin/Desktop/GEE_NTWK/gee_new.jpg', img)