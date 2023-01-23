import cv2
import sys

src = cv2.imread('field.bmp')
hero = cv2.imread('hero.png', cv2.IMREAD_UNCHANGED) # png 영상
print(hero.shape) # (64, 64, 4)

if src is None or hero is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

mask = hero[:,:,3] # 3에 해당하는 값은 (b,g,r)
hero = hero[:,:,:-1] # hero는 alpha값이 없어진 bgr 3채널, png는 4채널(b, g, r, a)이므로 마지막 a가 -1에 해당
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w]

cv2.copyTo(hero, mask, crop) # src 자리에는 투명도 있는 파일 오면 안됨. 그래서 위에서 투명도 없애준 것

cv2.imshow('src',src)
cv2.imshow('mask',mask)
cv2.imshow('hero',hero)
cv2.waitKey()
cv2.destroyAllWindows()