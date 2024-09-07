from flask import Flask, render_template, Response
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np
import math

app = Flask(__name__)

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector()

def generate_frames():
    while True:
        success, img = cap.read()
        if not success:
            break

        hands, img = detector.findHands(img)
        imgOutput = img.copy()

        if hands:
            hand = hands[0]
            x, y, w, h = hand['bbox']
            offset = 22
            imgCrop = img[max(y - offset, 0):min(y + h + offset, img.shape[0]),
                           max(x - offset, 0):min(x + w + offset, img.shape[1])]
            cv2.imshow("Image", img)

        # Encode the image as JPEG
        ret, buffer = cv2.imencode('.jpg', imgOutput)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('model.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)
