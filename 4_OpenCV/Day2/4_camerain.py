import cv2
import sys

cap = cv2.VideoCapture(0) # 기본 카메라 켜기

if not cap.isOpened():
    print('카메라를 열 수 없습니다')
    sys.exit()

print('가로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('세로 사이즈 : ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read() # return, frame

    if not ret: # return된 값이 없으면
        break # 즉시 코드 중지

    inversed = ~frame # 반전

    cv2.imshow('frame', frame) # 읽어온 frame을 보여줌
    cv2.imshow('inversed', inversed)  # 반전된 frame을 보여줌

    if cv2.waitKey(10) == 27: # 10 = 0.01초 (1000이 1초), 27 = ESC
        break

cap.release() # 카메라 끄기
cv2.destroyAllWindows()