import cv2
import sys

cap1 = cv2.VideoCapture('Lake.mp4')

if not cap1.isOpened():
    print('비디오를 열 수 없습니다')
    sys.exit()

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))

print('frame_cnt1 : ', frame_cnt1)
print('fps : ', fps)

out = cv2.VideoWriter('vid_output.avi', fourcc, fps, (w, h))

for i in range(frame_cnt1):
    ret1, frame1 = cap1.read()

    out.write(frame1)
    cv2.imshow('output', frame1)
    if cv2.waitKey(delay) == 27:
        break

cap1.release()
out.release()
cv2.destroyAllWindows()