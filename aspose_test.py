import cv2
from aspose.barcode import barcoderecognition
import numpy as np

def viwer(img):
    cv2.imshow('test',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def resize(img, n = 2):
    height, width = img.shape[:2]
    resized_image = cv2.resize(img, (width//n, height//n))
    
    return resized_image
    
def gray(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    return gray

def sharp(img):
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened_image = cv2.filter2D(img, -1, kernel)

    return sharpened_image


img_list = ["barcode_image2.jpg","barcode_image_1.jpg","barcode_image_2.jpg", "barcode_image_3.jpg"]
img_path = img_list[0]

# 원본 이미지
origin_image = cv2.imread(img_path)
reader = barcoderecognition.BarCodeReader(img_path)
recognized_results = reader.read_bar_codes()
for barcode in recognized_results:
    print(barcode.code_text)