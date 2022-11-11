from ast import arg
import io
import os
import argparse
from google.cloud import speech

# Perform streaming speech recognition on a local file
# Example:
# python3 demo_streaming_local.py audio_file_name

def transcribe_streaming(stream_file):
    client = speech.SpeechClient()

    with io.open(stream_file, 'rb') as audio_file:
        content = audio_file.read()

    stream = [content]

    requests = (
        speech.StreamingRecognizeRequest(audio_content=chunk) for chunk in stream
    )

    config = speech.RecognitionConfig(
        encoding='LINEAR16',
        sample_rate_hertz=16000,
        language_code='en-US'
    )

    streaming_config = speech.StreamingRecognitionConfig(config=config)

    responses = client.streaming_recognize(
        config=streaming_config,
        requests=requests
    )

    for response in responses:
        for result in response.results:
            print("Finished: {}".format(result.is_final))
            print("Stability: {}".format(result.stability))
            alternatives = result.alternatives
            # The alternatives are ordered from most likely to least.
            for alternative in alternatives:
                print("Confidence: {}".format(alternative.confidence))
                print(u"Transcript: {}".format(alternative.transcript))

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cloud_speech_to_text_service.json'
# transcribe_streaming('vietnamese_audio_test.wav')

if __name__ == "__main__":
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'cloud_speech_to_text_service.json'
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("stream", help="File to stream to the API")
    args = parser.parse_args()
    transcribe_streaming(args.stream)