import json
from vosk import Model, KaldiRecognizer
import os
import pyaudio


def speech_input():
    model_path = "./vosk-model-small-en-us-0.15" # Update this path to your model's location
    if not os.path.exists(model_path):
        print(
            "Model not present")
        exit(1)

    model = Model(model_path)
    rec = KaldiRecognizer(model, 16000)

    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    stream.start_stream()

    print("Please speak now...")

    while True:
        data = stream.read(4096)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = rec.Result()
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    result_dict = json.loads(result)
    return result_dict.get("text", "")


if __name__ == "__main__":
    print(speech_input())
