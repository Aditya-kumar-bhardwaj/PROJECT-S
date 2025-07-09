import pyttsx3  # Text-to-speech library
import speech_recognition as sr  # Speech recognition library
import datetime
import webbrowser
import os
import random

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
recognizer = sr.Recognizer()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to listen to user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            return ""
        except sr.RequestError as e:
            print("Could not request results. Check your network connection.")
            return ""

# Function to greet the user
def greet():
    current_time = datetime.datetime.now().time()
    if current_time < datetime.time(12):
        speak("Good morning! How can I assist you today?")
    elif datetime.time(12) <= current_time < datetime.time(18):
        speak("Good afternoon! How can I assist you today?")
    else:
        speak("Good evening! How can I assist you today?")

# Main program loop
greet()

while True:
    user_input = listen().lower()

    if "hello" in user_input:
        speak("Hello! How can I assist you today?")

    elif "how are you" in user_input:
        responses = ["I'm doing well, thank you.", "I'm just a computer program, but I'm functioning correctly.", "I'm here to help you, so I'm great!"]
        speak(random.choice(responses))

    elif "what's the time" in user_input or "tell me the time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}")

    elif "open website" in user_input:
        speak("Sure, please specify the website.")
        website = listen()
        webbrowser.open(website)

    elif "search" in user_input:
        speak("What would you like me to search for?")
        query = listen()
        search_url = f"https://www.google.com/search?q={query}"
        webbrowser.open(search_url)

    elif "exit" in user_input:
        speak("Goodbye!")
        break

    else:
        speak("I'm sorry, I didn't understand that command.")
