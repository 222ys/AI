import cv2
import sys

# 흑백 채널
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)
if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()
dst = cv2.add(src, 100)

# 컬러 채널
src2 = cv2.imread('lenna.bmp')
if src2 is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()
dst2 = cv2.add(src, (100,100,100,0))

cv2.imshow('src',src) # 흑백 원본
cv2.imshow('dst',dst) # 흑백 밝게
cv2.imshow('src2',src2) # 컬러 원본
cv2.imshow('dst2',dst2) # 컬러 밝게
cv2.waitKey()

