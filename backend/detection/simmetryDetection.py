import cv2
import numpy as np


def calculate(a, b):
    print(len(a))
    print(len(b))
    """Test the symmetry between two images by calculating the intersection/union of pixels"""

    intersection = cv2.bitwise_and(a, b)

    # cv2.imwrite('intersection.png', intersection)

    union = cv2.bitwise_or(a, b)

    # cv2.imwrite('union.png', union)

    res = cv2.countNonZero(intersection) / cv2.countNonZero(union)
    return res


def symmetry_detection2(im):
    # Read image in greyscale and get shape and centres
    im = cv2.imread(im, 0)
    h, w = im.shape
    ch, cw = h // 2, w // 2

    # Test left-right symmetry
    left = im[:, :cw]
    right = im[:, cw:]
    LR = calculate(left, np.flip(right, axis=1))

    # Test top-bottom symmetry
    top = im[:ch, :]
    bot = im[ch:, :]
    TB = calculate(top, np.flip(bot, axis=0))

    # Average
    symmetry = (LR + TB) / 2
    print(symmetry)
    return symmetry
