import cv2

img1 = cv2.imread('dog.jpg')
img2 = img1
img3 = img1.copy()

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

img2.fill(0)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

img1 = cv2.imread('dog.jpg')
img2 = img1[64:300, 165:450] # h, w
img3 = img1[64:300, 165:450].copy()

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()

img2.fill(0) # img2가 가리키는(=img1이 가리키는) 원본사진의 영역이 0으로 채워짐

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.waitKey()
cv2.destroyAllWindows()