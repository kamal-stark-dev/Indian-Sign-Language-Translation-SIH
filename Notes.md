## Indian Sign Language to text and speech conversion

HathSayBaat is a tool which helps the deaf and the hard-of-hearing community to translate their sign language into text and speech forms. It'll allow then to communicate better and removes the barrier to know sign language to understand and talk to the deaf and hard-of-hearing community.

![](./Prototype/assets/images/10100507.jpg)

Their are over 63 million deaf people in India (WHO Report), and this is not a small number. We all know they use sign languages to talk to others but not everyone knows sign language which makes it difficult for them to communicate with them. That's why to tackle this problem we have came up with a solution which is a website that can convert the Indian Sign Language into text and speech which can also be translated into multiple regional languages.

# Features

> 1. Real Time Translation
> 2. Multiple Languages Support
> 3. Video Call Integration
> 4. User Friendly Interface
> 5. Text to Speech

## TEXT TO SPEECH

> We can use libraries like `pyttsx3` and `gTTS` for converting the text to speech.

Using `pyttsx3`

> Installing `pyttsx3` -> `pip install pyttsx3`

```py
import pyttsx3

# Initialize the converter
engine = pyttsx3.init()

# Text to be converted
text = "Hello, welcome to Python text to speech conversion!"

# Convert text to speech
engine.say(text)

# Wait until the speech is finished
engine.runAndWait()
```

Using `gTTS`

> Install `gTTS` -> `pip install gtts`

```py
from gtts import gTTS
import os

# Text to be converted
text = "Hello, welcome to Python text to speech conversion!"

# Language in which you want to convert
language = 'en'

# Creating the gTTS object
tts = gTTS(text=text, lang=language, slow=False)

# Saving the converted audio in a mp3 file
tts.save("output.mp3")

# Playing the converted file (optional)
os.system("start output.mp3")  # Use 'afplay' on macOS or 'xdg-open' on Linux
```

## Translation in Multiple Languages

While talking about translation what better tool to use than `Google Translate`

Command - `pip install googletrans==4.0.0-rc1`

```py
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Text to be translated
text = "Hello, how are you?"

# List of Indian languages to translate into
languages = ['hi', 'bn', 'ta', 'te', 'mr', 'pa']  # Hindi, Bengali, Tamil, Telugu, Marathi, Punjabi

# Translate and print results
for lang in languages:
    translated = translator.translate(text, dest=lang)
    print(f'Translated to {lang}: {translated.text}')
```

### Creating a Structure and retreiving specific languages

```py
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Text to be translated
text = "Hello, my name is Kamalveer."

# List of Indian languages to translate into, including Punjabi
languages = ['hi', 'bn', 'ta', 'te', 'mr', 'pa']  # Hindi, Bengali, Tamil, Telugu, Marathi, Punjabi

# Create a dictionary to store translations
translations = {
    'en': {
        'text': text,
        'translations': {}
    }
}

# Translate and store results in the dictionary
for lang in languages:
    translated = translator.translate(text, dest=lang)
    translations['en']['translations'][lang] = translated.text

# Print the structured translations
print(translations)

# Specific language like Punjabi
punjabi_text = translations['en']['translations']['pa']
print(punjabi_text)
```

## Translation integration with the website

`html`

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Multilingual Website</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <div class="language-selector">
      <button id="language-icon">Change</button>
      <ul id="language-dropdown" class="dropdown">
        <li><a href="#" data-lang="en">English</a></li>
        <li><a href="#" data-lang="hi">हिन्दी</a></li>
        <li><a href="#" data-lang="bn">বাংলা</a></li>
        <li><a href="#" data-lang="ta">தமிழ்</a></li>
        <li><a href="#" data-lang="te">తెలుగు</a></li>
        <li><a href="#" data-lang="mr">मराठी</a></li>
        <li><a href="#" data-lang="pa">ਪੰਜਾਬੀ</a></li>
      </ul>
    </div>
    <div id="content">
      <h1 id="greeting">Hello, how are you?</h1>
    </div>
    <script src="script.js"></script>
  </body>
</html>
```

`CSS`

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
  background: #fff;
}

.language-selector {
  position: relative;
  display: inline-block;
}

#language-dropdown {
  display: none;
  position: absolute;
  background-color: white;
  border: 1px solid #ccc;
  z-index: 1;
}

#language-dropdown li {
  list-style: none;
}

#language-dropdown a {
  display: block;
  padding: 8px 12px;
  text-decoration: none;
  color: black;
}

#language-dropdown a:hover {
  background-color: #f1f1f1;
}
```

`JavaScript`

```js
// script.js
const translations = {
  en: {
    text: "Hello, how are you?",
  },
  hi: {
    text: "नमस्ते, आप कैसे हैं?", // Hindi
  },
  bn: {
    text: "হ্যালো, আপনি কেমন আছেন?", // Bengali
  },
  ta: {
    text: "வணக்கம், நீங்கள் எப்படி இருக்கிறீர்கள்?", // Tamil
  },
  te: {
    text: "హలో, మీరు ఎలా ఉన్నారు?", // Telugu
  },
  mr: {
    text: "नमस्कार, तुम्ही कसे आहात?", // Marathi
  },
  pa: {
    text: "ਸਤ ਸ੍ਰੀ ਅਕਾਲ, ਤੁਸੀਂ ਕਿਵੇਂ ਹੋ?", // Punjabi
  },
};

const languageIcon = document.getElementById("language-icon");
const languageDropdown = document.getElementById("language-dropdown");
const greeting = document.getElementById("greeting");

// Toggle dropdown visibility
languageIcon.addEventListener("click", () => {
  languageDropdown.style.display =
    languageDropdown.style.display === "block" ? "none" : "block";
});

// Change language on selection
languageDropdown.addEventListener("click", (event) => {
  event.preventDefault();
  const lang = event.target.getAttribute("data-lang");
  if (lang && translations[lang]) {
    greeting.textContent = translations[lang].text;
    languageDropdown.style.display = "none"; // Hide dropdown after selection
  }
});

// Close dropdown if clicked outside
window.addEventListener("click", (event) => {
  if (!event.target.matches("#language-icon")) {
    languageDropdown.style.display = "none";
  }
});
```

> Final Program - Takes user input and then translates into multiple languages and then converts their speech and saves them with appropriate names inside `audio_files` folder.

```py
from googletrans import Translator
from gtts import gTTS
import os
import pygame

# Initialize the translator
translator = Translator()

# Function to convert text to speech
def text_to_speech(text, lang='en', filename='output.mp3'):
    # Create a gTTS object
    tts = gTTS(text=text, lang=lang, slow=False)

    # Save the audio file
    audio_file = f"./audio_files/{filename}"
    tts.save(audio_file)

    # Initialize pygame mixer
    pygame.mixer.init()

    # Load and play the audio file
    pygame.mixer.music.load(audio_file)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        continue

# Main function
if __name__ == "__main__":
    # Create a directory for audio files if it doesn't exist
    if not os.path.exists('./audio_files'):
        os.makedirs('./audio_files')

    # Text to be translated
    text = str(input("Enter the text: "))

    # List of languages to translate into
    languages = ['hi', 'bn', 'ta', 'te', 'mr', 'pa', 'ur', 'fr']  # Hindi, Bengali, Tamil, Telugu, Marathi, Punjabi, Urdu

    # Create a dictionary to store translations
    translations = {
        'en': {
            'text': text,
            'translations': {}
        }
    }

    # Translate and store results in the dictionary
    for lang in languages:
        translated = translator.translate(text, dest=lang)
        translations['en']['translations'][lang] = translated.text

    # Print the structured translations
    print(translations)

    # Convert each translated text to speech and play it
    for lang, translated_text in translations['en']['translations'].items():
        lang_name = {
            'hi': 'Hindi',
            'bn': 'Bengali',
            'ta': 'Tamil',
            'te': 'Telugu',
            'mr': 'Marathi',
            'pa': 'Punjabi',
            'ur': 'Urdu'
        }.get(lang, 'English')

        print(f"Converting text to speech in {lang_name}: {translated_text}")
        text_to_speech(translated_text, lang=lang, filename=f"output_{lang_name}.mp3")
```

## Law and Justice usecase -

> As we know that in law system we need to hear both sides and their is a need of some tool which allows deaf and numb people to give their views and express their point to the judges and the lawyers. We can add commonly used law terms in our dataset and then train it on basis of that, to make it useful in the fields of law and justice.

### TODO - tasks to do for the project - For PROTOTYPE

_1. Starting Setup_

- [x] Install necessary libraries
- [x] Make a github Repo

_2. Model_

- [x] Setup the environment
- [x] Making program to collect and preprocess data
- [x] Creation of dataset

![](./Prototype/assets/images/notes/dataset-example.png)

_3. Website_

- [x] Design a website
- [x] Collecting the relevant images, videos & icons
- [x] Making the structure of the website

![](./Prototype/assets/images/notes/frontend-design.png)

- [x] Adding styles to the website
- [x] Adding dark-mode and scroll-up feature
- [x] Link to model page and style it
- [x] Add Social links like github and X (formerly twitter)
- [x] Integrate the model to website

![](./Prototype/assets/images/notes/multi-language-support.png)
