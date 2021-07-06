import cv2
import numpy as np


def irregularity_detection(img):
    # read image
    # img = cv2.imread('lemper2.png')

    # convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # threshold
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # invert
    thresh = 255 - thresh

    # get contours and compute average number of vertices per character (contour)
    result = img.copy()
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = contours[0] if len(contours) == 2 else contours[1]
    num_contours = 0
    sum = 0
    for cntr in contours:
        cv2.drawContours(result, [cntr], 0, (0, 0, 255), 1)
        num_vertices = len(cntr)
        sum = sum + num_vertices
        num_contours = num_contours + 1

    smoothness = (sum / num_contours)
    print(smoothness)

    # save resulting images
    # cv2.imwrite('lemper1_contours.png',result)
    # cv2.imwrite('lemper2_contours.png',result)

    # show thresh and result    
    # cv2.imshow("thresh", thresh)
    # cv2.imshow("contours", result)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
    return smoothness
