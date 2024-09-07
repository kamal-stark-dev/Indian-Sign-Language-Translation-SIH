from flask import Flask, render_template, Response
import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

app = Flask(__name__)

# Initialize video capture and hand detector
cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)

def generate_frames():
    while True:
        success, img = cap.read()
        if not success:
            break

        hands, img = detector.findHands(img)
        imgOutput = img.copy()

        if hands:
            for hand in hands:
                # Draw bounding box
                x, y, w, h = hand['bbox']
                cv2.rectangle(imgOutput, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green box

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
