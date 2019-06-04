import cv2
import numpy as np
from matplotlib import pyplot as plt

def segmentationf():
    img = cv2.imread('image.jpg', 0)

    ret, imgf = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)



    cv2.imshow('Image Segmentation',imgf)