import tkinter as tk
import threading
import speech_recognition as sr
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()

def speak(text):  
    engine = pyttsx3.init('sapi5')
    engine.say(text)
    engine.runAndWait()
    engine.stop()
     
def processCommand(c):
    if "open google" in c.lower():
        speak("opening google")
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        speak("opening Facebook")
        webbrowser.open('https://facebook.com')
    elif "open linkedin" in c.lower():
        speak("opening Linkedin")
        webbrowser.open('https://linkedin.com')
    elif "open youtube" in c.lower():
        speak("opening Youtube")
        webbrowser.open('https://youtube.com')
    elif "open whatsapp" in c.lower():
        speak("opening whatsapp")
        webbrowser.open('https://whatsapp.com')
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()
        if song in musicLibrary.music:
            speak(f"Playing {song}")
            webbrowser.open(musicLibrary.music[song])
        else:
            speak("Sorry, I could not find that song")

def voice_loop(status_label):
    speak("Initializing Alexa, a voice assistant")

    while True:
        try:
            status_label.config(text="Listening for wake word…")
            with sr.Microphone() as source:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)

            word = recognizer.recognize_google(audio)

            if word.lower() == "alexa":
                speak("Yes Anmol")
                status_label.config(text="Alexa Active…")

                with sr.Microphone() as source:
                    audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio)
                status_label.config(text=f"Command: {command}")
                processCommand(command)

        except Exception:
            pass
#GUI
def start_alexa(status_label, button):
    button.config(state=tk.DISABLED)
    t = threading.Thread(target=voice_loop, args=(status_label,), daemon=True)
    t.start()

root = tk.Tk()
root.title("Alexa Voice Assistant")
root.geometry("400x250")
root.configure(bg="#0f172a")

heading = tk.Label(root, text="Alexa Assistant", fg="white", bg="#0f172a",
                   font=("Segoe UI", 18, "bold"))
heading.pack(pady=20)

status_label = tk.Label(root, text="Idle", fg="#38bdf8", bg="#0f172a",
                        font=("Segoe UI", 12))
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start Alexa", font=("Segoe UI", 12, "bold"),
                         bg="#38bdf8", fg="black",
                         command=lambda: start_alexa(status_label, start_button))
start_button.pack(pady=20)

root.mainloop()