import cv2
import numpy as np
from matplotlib import pyplot as plt



def histogramf():
    img = cv2.imread('image.jpg')

    color = ('b', 'g', 'r')

    for i, col in enumerate(color):

        histr = cv2.calcHist([img], [i], None, [256], [0, 256])

        plt.plot(histr, color=col)

        plt.xlim([0, 256])

    plt.show()