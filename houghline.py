import cv2
import numpy as np

# _______________probabilistic hough line___________________

image = cv2.imread('su.png')
cv2.imshow('real',image)
print(image.shape)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,255,225,apertureSize=3)
lines = cv2.HoughLinesP(edges,1,np.pi /180,5)
print(lines)
for a in lines:
    print(a[0])
    x1, y1, x2, y2 = a[0]
    cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
cv2.imshow('probabilistic hough lines',image)
cv2.waitKey()
cv2.destroyAllWindows()