
# S.K.A.V.A - Sabesh Kumar's Advanced Voice Assistant

SKAVA (Sabesh Kumar's Advanced Voice Assistant) is a voice-activated assistant built using Python, designed to perform a variety of tasks such as web browsing, sending emails, playing music, and much more. It uses speech recognition, web scraping, and various APIs to enhance its functionality.

---

## 🚀 Setup Instructions

To set up and run SKAVA, follow the steps below:

### 1. Install Dependencies:
Make sure you have the following dependencies installed:

- **Python 3.x**
- **Required Python Libraries**:
  - `pyttsx3` (Text-to-speech conversion)
  - `speech_recognition` (Speech-to-text recognition)
  - `wikipedia` (Wikipedia API for querying information)
  - `wolframalpha` (API for knowledge-based queries)
  - `smtplib` (For sending emails)
  - `webbrowser` (To open websites)
  - `pygame` (For media controls)
  - `spotipy` (For Spotify music control)
  - `mutagen` (For handling MP3 metadata)
  - `omdb` (For querying movie information)

### 1. You can install all the dependencies with pip:
''' bash
pip install pyttsx3 speechrecognition wikipedia wolframalpha smtplib pygame spotipy mutagen omdb
'''

### 2. Configure the Application:
- **WolframAlpha API Key**: To use the WolframAlpha client, you'll need to create an account at [WolframAlpha](https://www.wolframalpha.com/) and get an API key. Replace `'LRWJW6-436RP7LH87'` in the code with your API key.
- **Email Configuration**: For sending emails, replace `Your_Username` and `Your_Password` with your Gmail credentials in the appropriate parts of the script.

### 3. Running the Program:
After setting up, simply run the script using Python:


SKAVA will start listening for commands and respond accordingly.

---

## 📁 Project Structure

- **`skava_assistant.py`**: The main Python script that drives SKAVA.
- **Libraries Used**:
  - **`pyttsx3`**: For text-to-speech conversion.
  - **`speech_recognition`**: To process speech input and convert it into text.
  - **`wikipedia`**: For getting summarized Wikipedia content.
  - **`wolframalpha`**: To answer advanced queries using WolframAlpha API.
  - **`smtplib`**: For sending emails via Gmail.
  - **`pygame`**: For music playback and media handling.
  - **`mutagen`**: For handling MP3 files and metadata.
  - **`spotipy`**: For controlling music on Spotify.

---

## 🛠️ Features & Usage

### 1. **Voice Commands**:
SKAVA can perform various tasks based on voice input. Below are some of the voice commands it can recognize:

- **Open websites**:
  - "Open YouTube"
  - "Open Google"
  - "Open Gmail"

- **Search Queries**:
  - "Search for [your query]" (Google search)
  - "What is [topic]?" (Wikipedia summary)
  - "What is the meaning of your name?" (Details about SKAVA)

- **Send Emails**:
  - "Email" (SKAVA will prompt for recipient and content)
  
- **Play Music**:
  - "Play music"
  - "Play English music"
  - "Play Tamil music"
  - "Play Hindi music"

- **Time and Date**:
  - "What time is it?"
  - "What date is it?"

- **General Queries**:
  - "Who is [name]?"
  - "Tell me a joke"
  - "Motivate me"

### 2. **Email Sending**:
SKAVA can send emails via Gmail. You'll need to provide your Gmail credentials for this feature to work.

### 3. **Music Playback**:
SKAVA can play music from a predefined folder or can play music from Spotify if configured with your Spotify account.

### 4. **System Control**:
You can control the system with commands like:
- "Stop" or "Exit" to close the assistant
- "Abort" to stop the program

---

## 🎨 Customization Ideas

- Add new commands to extend the functionality.
- Customize the greeting and responses for SKAVA.
- Add more services or APIs for integration.

---

## 🏗️ Built With

- **Python**: Core programming language for the assistant.
- **pyttsx3**: For text-to-speech functionality.
- **Speech Recognition**: For listening to user commands.
- **WolframAlpha**: For answering knowledge-based queries.
- **Wikipedia API**: For retrieving information from Wikipedia.
- **WebBrowser**: For opening websites.
- **Smtplib**: For sending emails.

---

## 📜 License

This project is open-source and available under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## 🎉 Acknowledgements

- **WolframAlpha API**: For providing detailed answers to user queries.
- **Wikipedia API**: For providing information on various topics.
- **Spotipy**: For integrating Spotify music control.
- **pyttsx3 and SpeechRecognition Libraries**: For enabling voice interaction with the assistant.

---

Enjoy using SKAVA, your personalized voice assistant!




