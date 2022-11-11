import os
from urllib import response
from google.cloud import speech

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cloud_speech_to_text_service.json'
speech_client = speech.SpeechClient()

# Eg 1: Transcribe Local Media File with google cloud speech to text v1
# File size: < 10 MB, length < 1 mins


## Step 1: Load the media files (en-US)
media_file_name_mp3 = 'vietnamese_audio_test.mp3'
media_file_name_wav = 'vietnamese_audio_test.wav'

with open(media_file_name_mp3, 'rb') as f1:
    byte_data_mp3 = f1.read()

audio_mp3 = speech.RecognitionAudio(content=byte_data_mp3)

with open(media_file_name_wav, 'rb') as f2:
    byte_data_mp3 = f2.read()

audio_wav = speech.RecognitionAudio(content=byte_data_mp3)

## Step 2: Configure Media Files Output
config_mp3 = speech.RecognitionConfig(
    encoding='LINEAR16',
    sample_rate_hertz=8000,
    enable_automatic_punctuation=True,
    language_code='vi-VN'
)

config_wav = speech.RecognitionConfig(
    encoding='LINEAR16',
    sample_rate_hertz=44100,
    enable_automatic_punctuation=True,
    language_code='vi-VN',
    audio_channel_count=1,
    enable_separate_recognition_per_channel=True
)

# Step 3:Transcribing the RecognitionAudio objects
response_standard_mp3 = speech_client.recognize(
    config=config_mp3,
    audio=audio_mp3
)

response_standard_wav = speech_client.recognize(
    config=config_wav,
    audio=audio_wav
)

print('This is response from mp3 file:')
print(response_standard_mp3)

print('This is response from wav file:')
print(response_standard_wav)

