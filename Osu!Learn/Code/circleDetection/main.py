import numpy as np
import cv2 as cv
import time
import matplotlib.pyplot as plt
from imgAiTrainer import Trainer


def edgesDetection():
    a = time.time()
    img = cv.imread('test.jpg', 0)
    edges = cv.Canny(img, 100, 200)
    b = time.time()
    print('temps :', round(b - a, 3), 'secondes')
    cv.imshow("Edges detection", edges)
    cv.waitKey()


def circlesDetection():
    a = time.time()
    img = cv.imread('img.png', 0)
    img = cv.GaussianBlur(img, (11, 11), 0)
    output = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    circles = cv.HoughCircles(img, cv.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=0, maxRadius=0)
    circles = np.uint16(np.around(circles))
    b = time.time()
    # for i in circles[0, :]:
    #     print('x :', i[0], 'y :', i[1], 'r :', i[2])
    #     cv.circle(output, (i[0], i[1]), i[2], (0, 255, 0), 2)
    #     cv.circle(output, (i[0], i[1]), 2, (0, 0, 255), 3)
    # # cv.imshow("Circles detection", output)
    # # cv.waitKey()
    # imgplot = plt.imshow(output)
    # plt.show()
    return (b-a)


tr = Trainer()
nbEssais = 10
temps = np.zeros(nbEssais)
for i in range(0, nbEssais):
    nbCercles = np.random.randint(1, 10)
    print(tr.createImg((800, 600), False, nbCercles))
    circlesDetection()
    temps[i] = circlesDetection()
tempsMoy = round(np.mean(temps), 4)
print('Temps de calcul moyen :', tempsMoy, 'secondes pour ', nbEssais, 'essais')