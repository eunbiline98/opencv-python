import cv2
import os
import numpy as np

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
body_classifier = cv2.CascadeClassifier("haarcascade_fullbody_default.xml")

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

RTSP_URL = (
    "rtsp://admin:padinet989@192.168.2.212:554/cam/realmonitor?channel=1&subtype=0"
)

os.environ["OPENCV_FFMPEG_CAPTURE_OPTIONS"] = "rtsp_transport;udp"

cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
# the output will be written to output.avi
out = cv2.VideoWriter("output.avi", cv2.VideoWriter_fourcc(*"MJPG"), 15.0, (640, 480))


if not cap.isOpened():
    print("Cannot open RTSP stream")
    exit(-1)

if cap.isOpened():
    width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)  # float `width`
    height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
    fps = cap.get(cv2.CAP_PROP_FPS)  # float `fps`
    total_frames = cap.get(
        cv2.CAP_PROP_FRAME_COUNT
    )  # float `total_frame_in_the_video` (should not be applicable for camera)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    # using a greyscale picture, also for faster detection
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(
        frame, winStride=(5, 5), padding=(3, 3), scale=1.21
    )
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, "Human Detection", (15, 50), font, 1, (0, 255, 255), 2)

    if len(boxes) == 0:
        teks = "User Terdeteksi = " + "0"
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, teks, (10, 470), font, 1, (0, 255, 255), 2)

    for xA, yA, xB, yB in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)
        roi_gray = gray[yA : yA + yB, xA : xA + xB]
        roi_color = frame[yA : yA + yB, xA : xA + xB]

        teks = "User Terdeteksi = " + str(len(boxes))
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, teks, (10, 470), font, 1, (0, 255, 255), 2)

    # Write the output video
    out.write(frame.astype("uint8"))
    # Display the resulting frame
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# When everything done, release the capture
cap.release()
# and release the output
out.release()
# finally, close the window
cv2.destroyAllWindows()
cv2.waitKey(1)
