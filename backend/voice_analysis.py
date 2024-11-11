
import speech_recognition as sr
from io import BytesIO
from text_analysis import analyze_text

def analyze_voice(audio_bytes: bytes):
    recognizer = sr.Recognizer()
    with sr.AudioFile(BytesIO(audio_bytes)) as source:
        audio = recognizer.record(source)
    recognized_text = recognizer.recognize_google(audio)
    analysis_result = analyze_text(recognized_text)
    return {"recognized_text": recognized_text, "analysis_result": analysis_result}
