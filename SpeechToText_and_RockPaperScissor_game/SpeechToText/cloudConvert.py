import speech_recognition as sr


def setup_speech_recognize(file_name: str, mode=1):
    """Converts english speech to text stored in audio format.

    This is wrapper function to SpeechRecognition library. Keyword argument
    `mode` switches between Google service and SphinxCMU service. The latter
    service does not require internet connection (accuracy gets compromised)

    Arguments
    ---------
    file_name : str
        Audio-file name containing english speech
    mode : int
        0 : OFFLINE mode
        1 : ONLINE mode (requires active internet connection) (default)
    """
    r = sr.Recognizer()
    audio_file = sr.AudioFile(file_name)
    with audio_file as source:
        audio = r.record(source)

    if mode:
        return _google_speech_recognize(r, audio)
    else:
        return _sphinx_speech_recognize(r, audio)


def _google_speech_recognize(r, audio):
    return r.recognize_google(audio)


def _sphinx_speech_recognize(r, audio):
    return r.recognize_sphinx(audio)
