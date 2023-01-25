import cv2
import sys
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 읽어올 수 없습니다')
    sys.exit()

alpha = 1.0
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)
# 이걸 해주는 이우: 기울기를 완만하게 해서 명암비를 보완해주려는 것
# 명암비 조절해주는 함수는 사용자 정의

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()