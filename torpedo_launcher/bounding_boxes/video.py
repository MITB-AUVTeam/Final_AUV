import cv2

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

fourcc = cv2.VideoWriter_fourcc(*'XVID')  
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))  

while True:
    ret, frame = cap.read()
    if not ret:
        break

    out.write(frame)

    cv2.imshow('Video Capture', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
