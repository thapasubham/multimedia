import cv2 as cv 

cam = cv.VideoCapture("ace.mp4") 
fps = cam.get(cv.CAP_PROP_FPS)
if fps == 0:
    fps = 30
delay = int(1000 / fps)
width = int(cam.get(cv.CAP_PROP_FRAME_WIDTH))
height = int(cam.get(cv.CAP_PROP_FRAME_HEIGHT)) 
while cam.isOpened():
    ret, frame = cam.read()
    if not ret:
        break

    cv.putText(frame, f"FPS: {fps:.2f}", (10, 30),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.putText(frame, f"Width: {width}", (10, 70),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.putText(frame, f"Height: {height}", (10, 110),
               cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv.imshow("video", frame)

    if cv.waitKey(delay) == ord('q'):
        break

cam.release()
cv.destroyAllWindows()