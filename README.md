<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Voice Assistant</title>
</head>
<body>
    <h1 style="text-align: center;">AI Voice Assistant</h1>
    <p align="center">
        <img src="https://img.shields.io/badge/Python-3.7%2B-blue" alt="Python Version">
        <img src="https://img.shields.io/badge/Status-Active-brightgreen" alt="Project Status">
        <img src="https://img.shields.io/badge/License-MIT-orange" alt="License">
    </p>

    <h2>About the Project</h2>
    <p>
        AI Voice Assistant is a Python-based virtual assistant designed to make your daily tasks easier. 
        It uses speech recognition and text-to-speech to respond to your commands and perform actions such as playing music, 
        fetching the weather, telling jokes, and much more.
    </p>

    <h2>Key Features</h2>
    <ul>
        <li>🎵 <b>Music Playback:</b> Plays your favorite songs directly from YouTube.</li>
        <li>⏰ <b>Time Information:</b> Tells the current time.</li>
        <li>☁️ <b>Weather Updates:</b> Provides current weather for any city.</li>
        <li>📰 <b>News Headlines:</b> Reads out the latest news headlines.</li>
        <li>🔍 <b>Wikipedia Search:</b> Retrieves short summaries for topics or people.</li>
        <li>😂 <b>Jokes:</b> Delivers funny and engaging jokes.</li>
        <li>➗ <b>Math Calculations:</b> Solves simple mathematical expressions.</li>
        <li>📝 <b>Notes:</b> Saves quick notes for later reference.</li>
        <li>🗣️ <b>Customizable Wake Word:</b> Trigger it with "Alexa" or modify as needed.</li>
    </ul>

    <h2>Prerequisites</h2>
    <ul>
        <li>Python 3.7 or above</li>
        <li>Libraries: 
            <ul>
                <li><code>pyttsx3</code></li>
                <li><code>speech_recognition</code></li>
                <li><code>pywhatkit</code></li>
                <li><code>wikipedia</code></li>
                <li><code>pyjokes</code></li>
                <li><code>requests</code></li>
            </ul>
        </li>
    </ul>

    <h2>Installation</h2>
    <ol>
        <li>Clone this repository:
            <pre><code>git clone https://github.com/your-username/ai-voice-assistant.git</code></pre>
        </li>
        <li>Navigate to the project directory:
            <pre><code>cd ai-voice-assistant</code></pre>
        </li>
        <li>Install the required libraries:
            <pre><code>pip install pyttsx3 speechrecognition pywhatkit wikipedia pyjokes requests</code></pre>
        </li>
        <li>Obtain API keys:
            <ul>
                <li>Sign up on <a href="https://openweathermap.org/" target="_blank">OpenWeatherMap</a> for a weather API key.</li>
                <li>Sign up on <a href="https://newsapi.org/" target="_blank">News API</a> for a news API key.</li>
            </ul>
        </li>
        <li>Replace the placeholders (<code>YOUR_API_KEY</code>) in the script with your keys.</li>
    </ol>

    <h2>Usage</h2>
    <p>Run the program using the following command:</p>
    <pre><code>python assistant.py</code></pre>
    <p>Speak commands such as:</p>
    <ul>
        <li>"Jarvis, play <i>song name</i>"</li>
        <li>"Jarvis, what's the weather in <i>city</i>?"</li>
        <li>"Jarvis, tell me a joke."</li>
        <li>"Jarvis, calculate <i>expression</i>."</li>
        <li>"Jarvis, what's the latest news?"</li>
    </ul>
    <p>To exit, say:</p>
    <ul>
        <li>"Jarvis, stop."</li>
        <li>"Jarvis, exit."</li>
    </ul>

    <h2>Contributing</h2>
    <p>Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.</p>

    <h2>License</h2>
    <p>This project is licensed under the <a href="LICENSE" target="_blank">MIT License</a>.</p>

    <h2>Acknowledgments</h2>
    <ul>
        <li>OpenAI for inspiring conversational AI projects.</li>
        <li>Libraries like Pyttsx3, SpeechRecognition, PyWhatKit, and others for enabling seamless functionality.</li>
    </ul>
</body>
</html>
