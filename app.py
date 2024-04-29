import pyttsx3
import datetime
import speech_recognition as sr
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


       # return "None"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/assistant', methods=['GET','POST'])
def assistant():
    def takeCommand():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print('Recognizing...')
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
            return query.lower()
        except Exception as e:
            print(e)
            print("Unable to recognize your voice.")
            speak("Unable to recognize your voice.")
    while True:
        query = takeCommand()
        
        hour = datetime.datetime.now().hour
        if 0 <= hour < 12:
            greeting = "Good Morning"
        elif 12 <= hour < 18:
            greeting = "Good Afternoon"
        else:
            greeting = "Good Evening"

        assname = "Jane"
        #speak(f"{greeting}, I am your Assistant {assname}. How can I help you?")
        

        if 'hello' in query:
            speak('hello, I am Jane your booking assistant')
            speak('how may I help you?')
        elif 'book an appointment' in query:
            speak('which department?')
        elif 'optical' in query:
            speak('okay..')
            speak('what is your name')
            uname = takeCommand()
            speak('Welcome to blue hospital')
            speak(uname)
            speak('time available is 9-11 and 5-6')
            speak('which time is good for you?')
        elif '9 to 11' in query:
            speak('your appointment has been booked for 9-11')
        elif '5 to 6' in query:
            speak('your appointment has been booked for 5-6')
        elif 'thank you' in query:
            speak('you are welcome')



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
