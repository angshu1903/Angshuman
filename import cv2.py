import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')
 
loaded_image = cv2.imread("/Users/angshu/Desktop/4444.jpg")
loaded_image = cv2.cvtColor(loaded_image,cv2.COLOR_BGR2RGB)
 
gray_image = cv2.cvtColor(loaded_image,cv2.COLOR_BGR2GRAY)
 
edged_image = cv2.Canny(gray_image, threshold1=30, threshold2=100)
 
 
plt.figure(figsize=(20,20))
plt.subplot(1,3,1)
plt.imshow(loaded_image,cmap="gray")
plt.title("Original Image")
plt.axis("off")
plt.subplot(1,3,2)
plt.imshow(gray_image,cmap="gray")
plt.axis("off")
plt.title("GrayScale Image")
plt.subplot(1,3,3)
plt.imshow(edged_image,cmap="gray")
plt.axis("off")
plt.title("Canny Edge Detected Image")
plt.show()