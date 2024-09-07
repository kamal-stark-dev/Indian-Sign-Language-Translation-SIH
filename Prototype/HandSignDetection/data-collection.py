import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math
import time

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Initialize hand detector
detector = HandDetector(maxHands=1)

# Offset for cropping
offset = 22

# image size define
imgSize = 300

folder_path = "Prototype\HandSignDetection\Signs\C"
counter = 0

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    # Find hands in the image
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']  # bbox = bounding box

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255 # np.uint8 -> unsigned integer of 8 bits = 0(black) to 255(white)

        # Calculate crop coordinates with boundary checks
        x_start = max(x - offset, 0)
        y_start = max(y - offset, 0)
        x_end = min(x + w + offset, img.shape[1])
        y_end = min(y + h + offset, img.shape[0])

        imgCrop = img[y_start:y_end, x_start:x_end]

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)

            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap: wCal + wGap] = imgResize # wgap -> width gap is used to center the image

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)

            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap: hCal + hGap, :] = imgResize


        cv2.imshow("Image Crop", imgCrop)
        cv2.imshow("Image White", imgWhite)

    # Display the image
    cv2.imshow("Image", img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
      counter += 1
      cv2.imwrite(f'{folder_path}/Image_{time.time()}.jpg', imgWhite)
      print(counter)


    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break

# Release the capture and destroy windows
cap.release()
cv2.destroyAllWindows()
