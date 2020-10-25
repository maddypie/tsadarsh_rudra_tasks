import requests

from .wavToFlac import wav_to_flac
from .cloudConvert import setup_speech_recognize
from .recordWrite import record_and_write


def speech_to_text(SECONDS=7):
    """Wrapper function returns english text from audio recorded through the
    microphone

    This funtion integrates `recordWrite`, `wavToFlac`, `cloudConvert` to a
    single call and returns the transcribed english text. Look into their
    specific files to get more detail on how it is done. Offline or Online
    speech recognisition service is invoked based on the network connection.
    Active internet connection uses `Google speech recognisition` services
    while SphinxCMU service is used if there is no interet connection.
    """

    file_name = record_and_write(SECONDS=SECONDS)
    converted_file_name = wav_to_flac(file_name)
    try:
        requests.get('https://google.com')
        text = setup_speech_recognize(converted_file_name)
    except requests.ConnectionError:
        text = setup_speech_recognize(converted_file_name, mode=0)
    with open('transcript.txt', 'w') as note:
        note.write(text)
    return text
