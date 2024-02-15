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
        face_detected = detect_faces()
        if face_detected:
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

                print("Monitoring face presence...")
                while detect_faces():
                    print("Face still detected.")
                    time.sleep(1)

                print("Face not detected. Waiting for 5 seconds before closing browser.")
                time.sleep(5)
                if not detect_faces():
                    print("Closing browser due to no face detected.")
                    close_orbix_project()
                else:
                    print("Face detected again. Not closing browser.")
            else:
                print("No relevant keywords found.")
        else:
            print("No face detected at the start.")
            time.sleep(1)  # Add a short wait to prevent the loop from spinning too fast when no face is detected.

if __name__ == "__main__":
    main()
