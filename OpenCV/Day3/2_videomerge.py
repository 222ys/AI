import cv2
import sys

cap1 = cv2.VideoCapture('Lake.mp4')
cap2 = cv2.VideoCapture('puma.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('비디오를 열 수 없습니다')
    sys.exit()

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
fourcc = cv2.VideoWriter_fourcc(*'DIVX')
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2 .get(cv2.CAP_PROP_FRAME_COUNT))

print('frame_cnt1 : ', frame_cnt1)
print('frame_cnt2 : ', frame_cnt2)
print('fps : ', fps)

out = cv2.VideoWriter('merge_output.avi', fourcc, fps, (w, h))

for i in range(frame_cnt1):
    ret1, frame1 = cap1.read()

    out.write(frame1)
    cv2.imshow('output', frame1)
    if cv2.waitKey(delay) == 27:
        break

for i in range(frame_cnt2):
    ret2, frame2 = cap2.read()

    out.write(frame2)
    cv2.imshow('output', frame2)
    if cv2.waitKey(delay) == 27:
        break

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()