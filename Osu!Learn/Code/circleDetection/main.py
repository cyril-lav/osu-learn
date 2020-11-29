import numpy as np
import cv2 as cv
import time
from imgAiTrainer import Trainer


def edgesDetection():
    a = time.time()
    img = cv.imread('test.jpg', 0)
    edges = cv.Canny(img, 100, 200)
    b = time.time()
    print('temps :', round(b-a, 3), 'secondes')
    cv.imshow("Edges detection", edges)
    cv.waitKey()

def circlesDetection():
    a = time.time()
    image = cv.imread("img.png", 0)
    output = cv.imread("img.png", 1)
    blurred = cv.GaussianBlur(image, (11, 11), 0)
    circles = cv.HoughCircles(blurred, cv.HOUGH_GRADIENT, 1, 100, param1=100, param2=90, minRadius=0, maxRadius=200)
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        b = time.time()
        for (x, y, r) in circles:
            print('x : ', x, ' y : ', y, ' r : ', r)
            cv.circle(output, (x, y), r, (0, 255, 0), 3)
            cv.rectangle(output, (x - 2, y - 2), (x + 2, y + 2), (0, 255, 0), -1)
    print('temps :', round(b - a, 3), 'secondes')
    cv.imshow("Circles detection", output)
    cv.waitKey()

tr = Trainer()
print(tr.createImg((800,600),False, 10))

# Commenter/décommenter l'un ou l'autre pour choisir entre
# la détection de cercle ou la détection de bordures

#edgesDetection()
circlesDetection()