from imutils.video import VideoStream
from flask import Response, Flask, render_template, request
import threading
import argparse
import imutils
import time
import cv2
from data import facedetect
import pickle
import numpy as np

outputFrame = None
lock = threading.Lock()

app = Flask(__name__)

vs = None
time.sleep(2)


@app.route("/")
def index():
    return render_template("index.html")


def detect_face(frameCount):
    global vs, outputFrame, lock

    data = pickle.loads(open('encodings.pickle', "rb").read())
    total = 0
    while True:
        frame = vs.read()
        if total > frameCount:
            face, confidence = facedetect.detect_face(frame)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            boxes = []
            names = []
            for idx, f in enumerate(face):
                box = (f[1], f[2], f[3], f[0])
                boxes.append(box)
            encodings = facedetect.face_encodings(rgb, boxes)

            for encoding in encodings:
                matches = facedetect.compare_faces(data["encodings"], encoding, tolerance=0.35)
                name = "Unknown"
                face_distances = facedetect.face_distance(data["encodings"], encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = data["names"][best_match_index]
                names.append(name)
            for ((top, right, bottom, left), name) in zip(boxes, names):
                cv2.rectangle(frame, (left - 20, top - 20), (right + 20, bottom + 20), (255, 0, 0), 2)

                # Draw a label with a name below the face
                cv2.rectangle(frame, (left - 20, bottom - 15), (right + 20, bottom + 20), (255, 0, 0), cv2.FILLED)
                font = cv2.FONT_HERSHEY_DUPLEX
                cv2.putText(frame, name, (left - 20, bottom + 15), font, 1.0, (255, 255, 255), 2)
        total += 1
        with lock:
            outputFrame = frame.copy()


def generate():
    global outputFrame, lock
    while True:
        with lock:
            if outputFrame is None:
                continue
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrame)

            if not flag:
                continue
        yield(b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + bytearray(encodedImage) + b'\r\n')


@app.route("/camera", methods=["GET"])
def camera():
    global vs
    data = request.args.get('data')
    if data == 'activate':
        vs = VideoStream(src=0).start()
    elif data == 'stop':
        vs = VideoStream(src=0).stop()


@app.route("/video_feed")
def video_feed():
    return Response(generate(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--ip", type=str, required=True,
                    help="ip address of the device")
    ap.add_argument("-o", "--port", type=int, required=True,
                    help="ephemeral port number of the server (1024 to 65535)")
    ap.add_argument("-f", "--frame-count", type=int, default=32,
                    help="# of frames used to construct the background model")
    args = vars(ap.parse_args())

    # start a thread that will perform motion detection
    t = threading.Thread(target=detect_face, args=(args["frame_count"],))
    t.daemon = True
    t.start()

    # start the flask app
    app.run(host=args["ip"], port=args["port"], debug=True,
            threaded=True, use_reloader=False)

# release the video stream pointer
vs.stop()