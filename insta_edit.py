import cv2.cv2
import numpy as np
from matplotlib import pyplot as plt
def threshold_val():
        img = cv2.cv2.imread('/home/durkesh/Downloads/duke.png',0)
        ret,thresh1 = cv2.cv2.threshold(img,150,150,cv2.cv2.THRESH_BINARY)
        ret,thresh2 = cv2.cv2.threshold(img,127,255,cv2.cv2.THRESH_BINARY_INV)
        ret,thresh3 = cv2.cv2.threshold(img,127,255,cv2.cv2.THRESH_TRUNC)
        ret,thresh4 = cv2.cv2.threshold(img,127,255,cv2.cv2.THRESH_TOZERO)
        ret,thresh5 = cv2.cv2.threshold(img,127,255,cv2.cv2.THRESH_TOZERO_INV)
        print(img.shape)
        titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
        images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
        display_colored(6,images,titles)
def adaptive_thresh():
    img = cv2.cv2.imread('/home/durkesh/Downloads/mitsubishi.jpg',0)
    img = cv2.cv2.medianBlur(img,1)
    ret,th1 = cv2.cv2.threshold(img,127,255,cv2.cv2.THRESH_BINARY)
    th2 = cv2.cv2.adaptiveThreshold(img,255,cv2.cv2.ADAPTIVE_THRESH_MEAN_C,cv2.cv2.THRESH_BINARY,11,2)
    th3 = cv2.cv2.adaptiveThreshold(img,255,cv2.cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.cv2.THRESH_BINARY,11,2)
    titles = ['Original Image', 'Global Thresholding ','Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
    images = [img, th1, th2, th3]
    display(4,images,titles)
def display(m,images,titles):
       for i in range(m):
            plt.subplot(4,3,i+1),plt.imshow(images[i],'gray')
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
       plt.show()
def display_colored(m,images,titles):
      for i in range(m):
            plt.subplot(4,3,i+1),plt.imshow(images[i])
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])
      plt.show()

def blur():
    img = cv2.cv2.imread('/home/durkesh/Downloads/mitsubishi.jpg',0)
    img1 = cv2.cv2.medianBlur(img,5)
    titles = ['Original Image', 'Blurred']
    images = [img, img1]
    display_colored(2,images,titles)
def hsv_text():
        covid = cv2.imread('/home/durkesh/Downloads/duke.png')
        covid=cv2.cvtColor(covid,cv2.COLOR_BGR2RGB)
        hsv_covid=cv2.cvtColor(covid,cv2.COLOR_RGB2HSV)
        hsv_low = (0,0,0)
        hsv_high = (300,200,200)
        mask = cv2.inRange(hsv_covid, hsv_low,hsv_high)
        return mask
def hsv_color():
        covid = cv2.imread('/home/durkesh/Downloads/duke.png')
        covid=cv2.cvtColor(covid,cv2.COLOR_BGR2RGB)
        hsv_covid=cv2.cvtColor(covid,cv2.COLOR_RGB2HSV)
        hsv_low = (0,0,0)
        hsv_high = (200,200,200)
        mask = cv2.inRange(hsv_covid, hsv_low,hsv_high)
        return mask
def switcher(argument):
    if argument==1:
        threshold_val()
    elif argument==2:
        adaptive_thresh()
    elif argument ==3:
        blur()
    elif argument==4:
        mask=hsv_text()
        plt.subplot(1, 2, 1)
        plt.imshow(mask, cmap="gray")
       

        plt.show()
    else:
        mask=hsv_color()
        
        plt.subplot(1, 2, 1)
        plt.imshow(mask)
     
        plt.show()
    
if __name__ == "__main__":
        argument=int(input("Select Function To Apply\nSelect 1 for Threshold Varient Filters\nSelect 2 Black and White Varients\nSelect 3 for Blur\nAlter the HSV Values in the CODE: \nSelect 4 for HSV(Text)\nSelect 5 for Coloured HSV"))
        switcher(argument)