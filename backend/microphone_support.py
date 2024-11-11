
import speech_recognition as sr

def listen_and_classify(recognizer, audio_model):
    """Listen to the user and classify the input for OCD tendencies."""
    try:
        print("Listening...")
        audio = recognizer.listen(audio_model)
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
