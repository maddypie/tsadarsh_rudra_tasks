import soundfile as sf


def wav_to_flac(file_name: str):
    """WAV audio file is converted to FLAC audio format

    File with `file_name` is loaded and converted to `flac` format using
    sound file library. Converted file name has is returned and has a `.flac`
    extension.

    Arguments
    ---------
    file_name : str
        WAV Audio-file name to convert
    """

    data, fs = sf.read(file_name)
    converted_file_name = file_name.partition('.')[0]+'.flac'
    sf.write(converted_file_name, data, fs)

    return converted_file_name
