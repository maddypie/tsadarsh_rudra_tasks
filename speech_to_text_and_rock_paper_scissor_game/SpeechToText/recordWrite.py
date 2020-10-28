import sounddevice as sd
from scipy.io.wavfile import write


def record_and_write(FS=44100, SECONDS=7):
    """Records audio through microphone for specified `SECONDS` (default : 7).
    Recorded audio is converted to a NumPy array and then stored in WAV format
    (temp.wav) in the working direcotry.

    Arguments
    ---------
    FS : int
        Recording sample rate (default: 44100)
    SECONDS : int
        Duration of recording in seconds (default : 7)
    """

    _start_screen(SECONDS)

    myrecording = sd.rec(int(SECONDS * FS), samplerate=FS, channels=2)
    sd.wait()

    _end_screen()

    file_name = "temp.wav"
    write(file_name, FS, myrecording)
    return file_name


def _start_screen(time: int):
    print(f"You have {time} seconds of recording")
    print("Start...")
    return


def _end_screen():
    print("Stopped.")
    return
