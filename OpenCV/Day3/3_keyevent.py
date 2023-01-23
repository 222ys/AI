import cv2

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)

while True:
    keyvalue = cv2.waitKey()
    if keyvalue == ord('i') or keyvalue == ord('I'): # 아스키코드 매핑. 대소문자 구분
        img = ~img
        cv2.imshow('image',img)
    elif keyvalue ==27: # ESC
        break

cv2.destroyAllWindows()