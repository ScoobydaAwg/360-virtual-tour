



# navigation.py
import webbrowser
import subprocess

def open_orbix_project(url="https://orbix360.com/_3L2pR10y"):
    webbrowser.open(url)

def close_orbix_project():
    # Close the Orbix project by killing the browser process
    subprocess.call(['taskkill', '/F', '/T', '/IM', 'chrome.exe'])




import spacy
import re

nlp = spacy.load("en_core_web_sm")

keywords_set = {"a", "b", "c"}

principal_pattern = re.compile(r"\b(principals?|principle)\b(?:'s)?(?: room| office)?", re.IGNORECASE)

def extract_keywords(text):
    doc = nlp(text)

    keywords = []
    for token in doc:

        token_text_lower = token.text.lower()


        if token_text_lower in keywords_set:
            keywords.append("block_" + token.text.upper())


        if principal_pattern.search(token_text_lower):
            keywords.append("principal")

    return keywords




import pyttsx3
from face import detect_faces
from speech import speech_input
from keywords import extract_keywords
from navigation import open_orbix_project

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        if detect_faces():
            choice = input("Face detected. Choose input method - Speech (S) or Manual (M): ").strip().upper()
            if choice == "S":
                input_text = speech_input()
            else:
                input_text = input("Enter your input manually: ")

            if input_text and extract_keywords(input_text):
                print("Sure, opening navigation to principal's office.")
                speak("Sure, opening navigation to principal's office.")
                open_orbix_project()

                # After the Orbix project is displayed, the chatbot closes and starts checking for the face again
                continue
            else:
                print("No relevant keywords found.")
        else:
            print("No face detected.")

if __name__ == "__main__":
    main()




import cv2 as cv

def detect_faces():
    capture = cv.VideoCapture(0)
    pretrained_model = cv.CascadeClassifier("facedata.xml")

    face_detected = False
    while True:
        ret, frame = capture.read()
        if not ret:
            break


        frame_small = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)

        gray = cv.cvtColor(frame_small, cv.COLOR_BGR2GRAY)
        faces = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

        if len(faces) > 0:
            face_detected = True
            break

    capture.release()
    cv.destroyAllWindows()
    return face_detected


import pyttsx3
from face import detect_faces
from speech import speech_input
from keywords import extract_keywords
from navigation import open_orbix_project, close_orbix_project
import time

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        if detect_faces():
            print("Face detected at the beginning.")
            choice = input("Face detected. Choose input method - Speech (S) or Manual (M): ").strip().upper()
            if choice == "S":
                input_text = speech_input()
            else:
                input_text = input("Enter your input manually: ")

            if input_text and extract_keywords(input_text):
                print("Keywords found. Opening navigation to principal's office.")
                speak("Opening navigation to principal's office.")
                open_orbix_project()

                # Continuously monitor face presence after opening the browser
                print("Monitoring face presence...")
                face_present = detect_faces()
                while face_present:
                    print("Face still detected.")
                    face_present = detect_faces()
                    time.sleep(1)

                print("Face not detected. Waiting for 5 seconds before closing browser.")
                time.sleep(5)  # Wait for 5 seconds before closing the browser
                if not detect_faces():
                    print("Closing browser due to no face detected.")
                    close_orbix_project()
                else:
                    print("Face detected again. Not closing browser.")

            else:
                print("No relevant keywords found.")
        else:
            print("No face detected at the start.")

if __name__ == "__main__":
    main()




import cv2 as cv
import logging

logging.basicConfig(level=logging.DEBUG)

def detect_faces():
    capture = cv.VideoCapture(0)
    pretrained_model = cv.CascadeClassifier("facedata.xml")

    while True:
        ret, frame = capture.read()
        if not ret:
            logging.debug("No frame captured.")
            break

        frame_small = cv.resize(frame, (0, 0), fx=0.5, fy=0.5)
        gray = cv.cvtColor(frame_small, cv.COLOR_BGR2GRAY)
        faces = pretrained_model.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4, minSize=(30, 30))

        logging.debug(f"Faces detected: {len(faces)}")

        if len(faces) > 0:
            capture.release()
            cv.destroyAllWindows()
            return True
        else:
            capture.release()
            cv.destroyAllWindows()
            return False
