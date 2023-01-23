import cv2
import numpy as np

img = np.full((400,400,3),255,np.uint8) # 400x400짜리 컬러채널에 흰색으로 채움

cv2.line(img, (50,50), (200,50), (0,0,255), 5) # img, 시작, 끝, 색상, 굵기

cv2.rectangle(img, (50,200,150,100), (0,255,0), 2) # img, 사각형위치, 색상, 굵기
cv2.rectangle(img, (70,220,180,100), (0,120,0), -1)

cv2.circle(img, (300,10), 50, (255,255,0), -1) # img, 중점, 반지름, 색상, 굵기

text = 'Hello, Python'
cv2.putText(img, text, (50,350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255))
# img, 텍스트, 좌측하단좌표, 폰트, 폰트크기, 색상

cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()