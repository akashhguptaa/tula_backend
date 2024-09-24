import pyttsx3 as pt
import speech_recognition as sr

r = sr.Recognizer()
def text_to_speech(command):
    # Initialize the engine
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 200)
        engine.setProperty('Volume', 2.0)
        engine.say(command) 
        engine.runAndWait()

    except Exception as e:
        print(f"Exception {e} has occured")

def speech_to_text():
    try:
        # using microphone as source for input.
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
                 
            audio = r.listen(source)   
            MyText = r.recognize_google(audio)
            MyText = MyText.lower()

    except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
    except sr.UnknownValueError:
            print("unknown error occurred")
            
