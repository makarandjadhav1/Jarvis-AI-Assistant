import pywhatkit
import datetime
import wikipedia
import pyjokes
import requests
import speech_recognition as sr
import pyttsx3
import math

# Initialize text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Function to convert text to speech
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize voice commands
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
                print(f"Command: {command}")
                return command
    except Exception as e:
        print(f"Error: {e}")
        return ""
    return ""

# Get current weather
def get_weather(city):
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url).json()
    if response.get('main'):
        temp = response['main']['temp']
        weather = response['weather'][0]['description']
        talk(f"The current temperature in {city} is {temp}°C with {weather}.")
    else:
        talk("Sorry, I couldn't find the weather information for that city.")

# Fetch latest news
def get_news():
    api_key = 'YOUR_API_KEY'  # Replace with your News API key
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()
    articles = response.get('articles', [])
    if articles:
        talk("Here are the latest news headlines:")
        for i, article in enumerate(articles[:5], 1):
            talk(f"{i}. {article['title']}")
    else:
        talk("Sorry, I couldn't fetch the news right now.")

# Perform math operations
def calculate(command):
    try:
        result = eval(command)
        talk(f"The result is {result}")
    except:
        talk("Sorry, I couldn't perform the calculation.")

# Run the assistant
def run_alexa():
    talk("Hello, how can I assist you?")
    while True:
        command = take_command()
        if not command:
            continue

        if 'play' in command:
            song = command.replace('play', '').strip()
            talk(f"Playing {song}")
            pywhatkit.playonyt(song)

        elif 'time' in command:
            current_time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The current time is {current_time}")

        elif 'weather' in command:
            city = command.replace('weather', '').strip()
            get_weather(city)

        elif 'news' in command:
            get_news()

        elif 'who is' in command:
            person = command.replace('who is', '').strip()
            info = wikipedia.summary(person, sentences=2)
            talk(info)

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            talk(joke)

        elif 'calculate' in command:
            expression = command.replace('calculate', '').strip()
            calculate(expression)

        elif 'note' in command:
            talk("What would you like me to note?")
            note = take_command()
            with open("notes.txt", "a") as file:
                file.write(note + "\n")
            talk("Noted!")

        elif 'stop' in command or 'exit' in command:
            talk("Goodbye! Have a great day!")
            break

# Start the assistant
if __name__ == "__main__":
    run_alexa()
