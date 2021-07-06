import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnchoredText


def detect_diameter(img_src):
    thresh = cv2.imread(img_src, 0)
    contours, hierarchy = cv2.findContours(thresh, 2, 1)
    thresh = cv2.cvtColor(thresh, cv2.COLOR_GRAY2RGB)
    # print (len(contours))
    cnt = contours

    for i in range(len(cnt)):
        (x, y), radius = cv2.minEnclosingCircle(cnt[i])
        center = (int(x), int(y))
        radius = int(radius)
        cv2.circle(thresh, center, radius, (0, 255, 0), 2)
        print((radius * 2) / 100)
        return (radius * 2) / 100

    # print ('Circle: ' + str(i) + ' - Center: ' + str(center) + ' -     Radius: ' + str(radius))

    # plt.text(x-15, y+10, '+', fontsize=25, color = 'red')
    # plt.text(10, -10, 'Centro: '+str(center), fontsize=11, color = 'red')
    # plt.text(340, -10, 'Diametro: '+str((radius*2)/100)+'mm', fontsize=11, color = 'red')

    # plt.Circle(x, y, color='red', fill=False)
    # plt.imshow(thresh, cmap='gray')
    # plt.show()
