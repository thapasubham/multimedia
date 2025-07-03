import cv2
import numpy as np

cap = cv2.VideoCapture("ace.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
delay = int(100 / fps)
i = 1
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to HSV for color manipulation
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Random hue shift amount between -20 and 20
    hue_shift = random.randint(-20, 20)

    # Apply hue shift and wrap around with modulo 180 (hue range)
    hsv[:, :, 0] = (hsv[:, :, 0].astype(int) + hue_shift) % 180

  

    # Enemy color mask (red detection)
    lower_red1 = np.array([0, 120, 70])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 120, 70])
    upper_red2 = np.array([180, 255, 255])

    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask = mask1 + mask2

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) > 5000:
            x, y, w, h = cv2.boundingRect(cnt)
            # Draw rectangles on the hue-shifted frame
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 2, 255), 3)
            cv2.putText(frame, "ENEMY", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 2, 255), 2)

    cv2.imshow("Trippy Enemy Detector", frame)
    cv2.imwrite(f"ace/frame_{i}.jpg", frame)
    i += 1
    if cv2.waitKey(delay) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()