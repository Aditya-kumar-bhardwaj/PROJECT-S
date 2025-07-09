import pyttsx3  # Text-to-speech library
import speech_recognition as sr  # Speech recognition library
import datetime

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

# Main program loop
while True:
    user_input = listen().lower()

    if "hello" in user_input:
        speak("Hello! How can I assist you today?")

    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "exit" in user_input:
        speak("Goodbye!")
        break

    else:
        speak("I'm sorry, I didn't understand that command.")
