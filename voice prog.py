import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import os

# init pyttsx
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")

engine.setProperty('voice', voices[1].id)  # 1 for female and 0 for male voice


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said:" + query + "\n")
    except Exception as e:
        print(e)
        speak("I didnt understand")
        return "None"
    return query


if __name__ == '__main__':

    speak("Baby assistance activated ")
    speak("How can i help you")
    while True:
        query = take_command().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia ...")
            query = query.replace("wikipedia", '')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)
        elif 'are you' in query:
            speak("I am Baby developed by peddababu")
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            speak("opening google")
            webbrowser.open("google.com")
        elif 'open github' in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif 'open stackoverflow' in query:
            speak("opening stackoverflow")
            webbrowser.open("stackoverflow.com")
        elif 'open spotify' in query:
            speak("opening spotify")
            webbrowser.open("spotify.com")
        elif 'open whatsapp' in query:
            speak("opening whatsapp")
            loc = "C:\\Users\\jaspr\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(loc)
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'play music' in query:
            speak("opening music")
            webbrowser.open("spotify.com")
        elif 'local disk d' in query:
            speak("opening local disk D")
            webbrowser.open("D://")
        elif 'local disk c' in query:
            speak("opening local disk C")
            webbrowser.open("C://")
        elif 'local disk e' in query:
            speak("opening local disk E")
            webbrowser.open("E://")
        elif 'sleep' in query:
            exit(0)
'''
#########
## About The Project
  Console Application which help to do your daily work routine.

Why Amigo:
* It can search on wikipedia.
* It can open YouTube, Spotify, Whatsapp (if installed on your pc) and other cool stuff.
* You can easily add your command.


### Built With

* Python 3


<!-- USAGE EXAMPLES -->
## Usage
1. It is easy to use just you need is basic Python knowledge
2. You can add your command inside main method by appending ladder if statements.

```
elif 'YOUR VOICE COMMAND' in query:
            speak("YOUR COMMAND")
            ## YOUR CODE
```


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch 
3. Commit your Changes
4. Push to the Branch
5. Open a Pull Request






<!-- CONTACT -->
## Contact
LinkedIn
[peddababu](https://www.linkedin.com/in/peddababu-naik-853197244)


<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
* Python 3 language
* wikipedia library
* pyttsx3 library
* os library
* speech_recognition library
* webbrowser library
######################################################################################################################################################################################################





This code appears to be a simple voice-controlled assistant that can perform various tasks. Here's what it does:

1. Imports required libraries: The code imports several libraries, including `pyttsx3` for text-to-speech synthesis, `speech_recognition` for speech recognition, `wikipedia` for searching Wikipedia articles, `webbrowser` for opening web pages, and `os` for interacting with the operating system.

2. Initializes the text-to-speech engine: The code initializes the `pyttsx3` text-to-speech engine and sets the voice to be used (a female voice).

3. Defines functions:
   - `speak(audio)`: Takes a string as input and uses the text-to-speech engine to speak it aloud.
   - `take_command()`: Listens to the user's voice input through the microphone, recognizes it using the Google Speech Recognition API, and returns the recognized query.

4. Main script:
   - It starts by greeting the user and asking for their query.
   - It enters an infinite loop to listen to the user's commands continuously.
   - If the user's query contains "wikipedia," it will try to search Wikipedia and read the summary of the topic to the user.
   - If the query contains specific keywords like "open youtube," "open google," "open github," "open stackoverflow," "open spotify," "open whatsapp," "play music," "local disk D," "local disk C," or "local disk E," the assistant will perform the corresponding action, such as opening the respective web page or the file explorer for the specified disk drive.
   - If the user says "sleep," the program will terminate and exit.

Overall, this script provides a basic voice-controlled assistant capable of performing simple tasks like searching Wikipedia, opening websites, and accessing files on the local disk. However, it is important to note that there are no error-handling mechanisms for possible API failures or user input errors, which could be added to make the assistant more robust. Additionally, the `pyttsx3` library may require further setup and configuration depending on the platform being used.
'''