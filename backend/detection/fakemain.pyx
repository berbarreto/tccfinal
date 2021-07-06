from cropImage import crop_center
from colorDetection import color_pallete
from borderDetection import border_detection
from simmetryDetection import symmetry_detection
from irregularityDetection import irregularity_detection
from diamaterDetection import diameter_detection
import cv2

img_path = 'image2.jpg'
img_normal = cv2.imread(img_path)
img_cropped = crop_center(img_normal)
img_pallete = color_pallete(img_path)

img_border = border_detection(img_cropped)
img_symmetry = symmetry_detection(img_path)
img_irregularity = irregularity_detection(img_cropped)
img_diameter = diameter_detection(img_path)
