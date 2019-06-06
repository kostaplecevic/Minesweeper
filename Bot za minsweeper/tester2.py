import pyautogui
import time
import cv2
import numpy as np
from matplotlib import pyplot as plt
import pickle

def screenshot(): #slika ekran
    pyautogui.screenshot('screen.png')

screenshot()

import cv2
import numpy as np
from matplotlib import pyplot as plt

brojac = 0

img_rgb = cv2.imread('screen.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
template = cv2.imread('number1.png',0)
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.92
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
    print(pt)
    brojac+=1
    pyautogui.moveTo(pt)
cv2.imwrite('res.png',img_rgb)

print(brojac)