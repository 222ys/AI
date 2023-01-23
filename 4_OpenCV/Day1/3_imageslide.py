import cv2
import sys
import glob

imgs = glob.glob('images\\*.jpg')
# print(imgs)

if not imgs:
    print('영상을 불러올 수 없습니다')
    sys.exit()

idx = 0
while True:
    img = cv2.imread(imgs[idx])

    if img is None:
        print('영상을 불러올 수 없습니다')
        break

    cv2.imshow('image',img) # 창 이름이 image, 내용은 img
    if cv2.waitKey(1000) >= 0: # 1초(1000밀리세컨드) 안에 key를 누르면 밖으로 나감, 어떤 키를 눌러도 아스키코드에 의해 0보다 큼
        break

    idx +=1
    if idx >= len(imgs):
        idx = 0 # 다시 처음 사진으로 돌아가 무한루프

cv2.destroyAllWindows()