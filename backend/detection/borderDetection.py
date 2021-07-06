import cv2
import numpy as np
import matplotlib.pyplot as plt


def border_detection(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    elementoEstruturante = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    metodo = cv2.THRESH_BINARY_INV
    ret, imgb = cv2.threshold(img_gray, 100, 255, metodo)

    img_morph = cv2.dilate(imgb, elementoEstruturante, iterations=1)

    img_edge = cv2.Canny(img_morph, 120, 200)

    ret3, thresh = cv2.threshold(img_edge, 127, 255, 0)
    contours, hierarchy = cv2.findContours(thresh, 2, 1)
    cnt1 = contours[0]

    # plt.plot(122),plt.imshow(img_edge, cmap='gray', vmin= 0, vmax= 255)
    # plt.title('Morphed Image'), plt.xticks([]), plt.yticks([])
    # plt.show()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return img_edge
