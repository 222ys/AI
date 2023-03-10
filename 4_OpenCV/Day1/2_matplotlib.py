import cv2
import matplotlib.pyplot as plt

img = cv2.imread('cat.bmp') # 컬러 영상(blue,green,red)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # BGR -> RGB

# plt.axis('off')# 격자 감추기
# plt.imshow(img)
# plt.show()

img_gray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE) # 흑백 영상

# plt.axis('off') # 격자를 감춤
# plt.imshow(img_gray, cmap='gray')
# plt.show()

plt.subplot(121) # 1행 2열의 1번 인덱스
plt.axis('off')
plt.imshow(img)

plt.subplot(122)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')

plt.show()