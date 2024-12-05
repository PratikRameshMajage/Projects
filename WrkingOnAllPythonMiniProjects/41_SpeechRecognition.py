import speech_recognition as sr

# create a recognizer instance
r = sr.Recognizer()

# use the microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    # listen for audio and convert it to text
    audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print(f"You said: {text}")
    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
