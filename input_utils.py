# import the necessary packages

from pyimagesearch import imutils
import numpy as np
from PIL import Image as Pim
from PIL import ImageOps
import math
import cv2
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join

def showImg(img, size=0, color=cv2.COLOR_BGR2RGB):
    """
    plots image in jupyter notebook inline
    takes optional args size and color (gray vs BGR is normal useage)
    """
    rgb_img = cv2.cvtColor(img, color)
    if (size != 0):
        width = size
        height = size
        plt.figure(figsize=(size, size))
        plt.imshow(rgb_img)
    else:
        plt.figure()
        plt.imshow(rgb_img)

def get_images(mypath, stack=False):
    onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
    images = np.empty(len(onlyfiles), dtype=object)
    onlyfiles = sorted(onlyfiles)
    for n in range(0, len(onlyfiles)):
        images[n] = cv2.imread( join(mypath,onlyfiles[n]))
        #if n > 1:
            #stacked = np.stack((stacked,images[n])s)
    if stack:
        return images,stacked
    else:
        return images

def crop(img, top, left, bot=-1, right=-1):
    if (bot == -1):
        bot = top
    if (right == -1):
        right = left

    height = img.shape[0] #height
    width = img.shape[1]
    return img[top:(height - bot), left:(width - right)]

def expand_rect(p, rect):
    rect[0]    -= p
    rect[1][0] += p
    rect[1][1] -= p
    rect[2]    += p
    rect[3][0] -= p
    rect[3][1] += p
    return rect
