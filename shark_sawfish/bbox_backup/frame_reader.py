import os
import cv2

save_dir = os.path.expanduser('~/Documents/frames')
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture('output.mp4')

frame_count = 0
while True:
    ret, frame = cap.read()
    if not ret:
        break  

    frame_filename = os.path.join(save_dir, f'frame_{frame_count:05d}.jpg')
    cv2.imwrite(frame_filename, frame) 
    frame_count += 1

cap.release()
print(f"Saved {frame_count} frames to {save_dir}")
