import cv2
import numpy as np

# 전역변수
oldx = oldy = -1 # 0도 좌표에 들어가기 때문에 아예 좌표에 안 들어가 있게끔 음수값 넣어줌

def on_mouse(event, x, y, flags, param):
    global oldx, oldy # global : 전역변수 사용

    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽버튼이 눌렸다면
        oldx, oldy = x, y # 눌린 곳의 x,y좌표
        print('왼쪽 버튼 클릭: %d, %d' % (x,y))

    elif event == cv2.EVENT_LBUTTONUP: # 마우스 왼쪽버튼이 떼졌다면
        print('왼쪽 버튼 뗌: %d, %d' % (x,y))

    elif event == cv2.EVENT_MOUSEMOVE: # 마우스 커서가 움직였다면
        if flags & cv2.EVENT_FLAG_LBUTTON: # 마우스 이벤트가 벌어지고 있는 상황에서, 왼쪽버튼이 눌러져 있다면
            cv2.line(img, (oldx,oldy), (x,y), (255,51,255), 3, cv2.LINE_AA)
            cv2.imshow('image', img)
            oldx, oldy = x, y

img = np.ones((480,640,3), dtype=np.uint8) * 255 # ones여서 검정색이었다가 255 곱해서 흰색됨

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img) # on_mouse: 내가 만들 콜백함수 이름

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()