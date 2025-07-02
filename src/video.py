import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()

prev_frame = None   # Previous processed frame
prev1_frame = None  # Frame before prev_frame (two-frames ago)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame. Exiting ...")
        break

    # Initialize prev_frame and prev1_frame
    if prev_frame is None:
        prev_frame = frame.copy()
        continue
    if prev1_frame is None:
        prev1_frame = prev_frame.copy()
        continue

 
    temp = cv.addWeighted(frame, 0.5, frame, 0.6, 0)

    temp1 = cv.addWeighted(frame, 0.5, prev1_frame, 0.6, 0)

    blended = cv.addWeighted(temp1, 0.5, prev_frame, 0.5, 0)
   
    #split the rgb channels
    b, g, r = cv.split(blended)
    bT, gT, rT = cv.split(temp1)
    b2, g2, r2 = cv.split(temp)

    #perform operation in the rgb channels
    rV = cv.bitwise_or(r, rT)
    bV = cv.bitwise_xor(b, bT)
    gV = cv.bitwise_or(g, gT)

    r_mix = cv.bitwise_or(rV,r2)
    b_mix = cv.bitwise_or(bV, b2)
    g_mix = cv.bitwise_or(gV, g2)

    #merge the rgb channels
    merge1 = cv.merge((b, gT,r2))
    final = cv.merge((bT,g_mix,r_mix))

    #copy the frame data 
    prev1_frame = prev_frame.copy()
    prev_frame = merge1.copy()

    cv.imshow('merge1', merge1)
    cv.imshow("final", final)
    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()
