import datetime
import webbrowser
import pywhatkit
import pyttsx3
import os

print("=== Personal AI Assistant ===")

def speak(text):
    print("Assistant:", text)

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

while True:
    command = input("You: ").lower()

    if command == "exit":
        speak("Goodbye!")
        break

    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(current_time)

    elif "date" in command:
        today = datetime.date.today()
        speak(str(today))

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        speak("Opening YouTube")

    elif "open google" in command:
        webbrowser.open("https://google.com")
        speak("Opening Google")

    elif "search" in command:
        search_item = command.replace("search", "")
        pywhatkit.search(search_item)
        speak("Searching for " + search_item)

    elif "play" in command:
        song = command.replace("play", "")
        pywhatkit.playonyt(song)
        speak("Playing " + song)

    elif "open notepad" in command:
        os.system("notepad")
        speak("Opening Notepad")

    elif "open calculator" in command:
        os.system("calc")
        speak("Opening Calculator")

    elif "send whatsapp message" in command:

    phone = input("Enter phone number: ")
    message = input("Enter message: ")

    pywhatkit.sendwhatmsg(
        phone,
        message,
        19,
        12
    )

    speak("Sending WhatsApp message")

    else:
        speak("I don't understand.")