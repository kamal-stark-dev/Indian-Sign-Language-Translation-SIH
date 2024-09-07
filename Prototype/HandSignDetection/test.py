import cv2
from cvzone.HandTrackingModule import HandDetector
# from cvzone.ClassificationModule import Classifier
import numpy as np
import math

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Suppresses most TensorFlow logs
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'  # Disables oneDNN optimizations

# Initialize video capture
cap = cv2.VideoCapture(0)
cap.set(3, 1280)  # Set width
cap.set(4, 720)   # Set height

# Initialize hand detector and classifier
detector = HandDetector(maxHands=1)
# classifier = Classifier(r"C:\Users\91638\Desktop\Projects\Github\Indian-Sign-Language-Translation-SIH\Prototype\HandSignDetection\Model\keras_model.h5",r"C:\Users\91638\Desktop\Projects\Github\Indian-Sign-Language-Translation-SIH\Prototype\HandSignDetection\Model\labels.txt")

# Offset for cropping
offset = 22
imgSize = 300  # Image size

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image")
        break

    imgOutput = img.copy()

    # Detect hands in the image
    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']  # bbox = bounding box

        # Calculate crop coordinates with boundary checks
        x_start = max(x - offset, 0)
        y_start = max(y - offset, 0)
        x_end = min(x + w + offset, img.shape[1])
        y_end = min(y + h + offset, img.shape[0])

        imgCrop = img[y_start:y_end, x_start:x_end]

        if imgCrop.size > 0:  # Ensure the crop is valid
            # Create a white background image
            imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
            aspectRatio = h / w

            if aspectRatio > 1:
                # Height is greater, fit to height
                k = imgSize / h
                wCal = math.ceil(k * w)
                imgResize = cv2.resize(imgCrop, (wCal, imgSize))
                wGap = math.ceil((imgSize - wCal) / 2)
                imgWhite[:, wGap:wCal + wGap] = imgResize

            else:
                # Width is greater, fit to width
                k = imgSize / w
                hCal = math.ceil(k * h)
                imgResize = cv2.resize(imgCrop, (imgSize, hCal))
                hGap = math.ceil((imgSize - hCal) / 2)
                imgWhite[hGap:hCal + hGap, :] = imgResize

            # Perform classification
            # prediction, index = classifier.getPrediction(img)
            # print("Prediction: ", prediction, " index: ", index)

            # Show cropped and white background images
            cv2.imshow("Image Crop", imgCrop)
            cv2.imshow("Image White", imgWhite)

    # Display the original image
    cv2.imshow("Image", imgOutput)

    # Exit loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
