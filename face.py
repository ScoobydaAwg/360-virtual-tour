import cv2 as cv

def detect_faces():
    capture = cv.VideoCapture(0)
    pretrained_model = cv.CascadeClassifier("facedata.xml")
    ret, frame = capture.read()
    if ret:
        frame_small = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
        gray = cv.cvtColor(frame_small, cv.COLOR_BGR2GRAY)
        faces = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))
        capture.release()
        cv.destroyAllWindows()
        return len(faces) > 0
    capture.release()
    cv.destroyAllWindows()
    return False
