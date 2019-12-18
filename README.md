# Robotics Speech

## Requirements
* [Anaconda](https://www.anaconda.com/)
* [SpeechRecognition](https://github.com/Uberi/speech_recognition)

## Installation

```bash
sudo apt-get install swig libpulse-dev libasound2-dev portaudio19-dev python-pyaudio python3-pyaudio espeak
conda create -n robotics-speech python=3.7.3
conda activate robotics-speech
pip install -r requirements.txt
```

Open a python terminal and run:

```python
import nltk
nltk.download('punkt')
```

## Running

```bash
conda activate robotics-speech
python src/main.py
```