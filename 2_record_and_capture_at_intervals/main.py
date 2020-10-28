import numpy as np
import cv2
import time
import os


def startapp(SOURCE: int=0, CAPTURE_INTERVAL: int=3,
             FR: float=20.0, OUTPUT :str='output.avi',
             CODEC: str='XVID', WAIT_KEY: int=25):
    """Captures video through video input source.

    Default `SOURCE` is inbuilt webcam; specify external camera by setting
    `SOURCE` other than 0. Frames are captured every `CAPTURE_INTERVAL` seconds
    and stored with `frame[\d].png` name.

    Arguments
    ---------
    SOURCE: int
        Video recording source
    CAPTURE_INTERVAL: int
        Time interval in seconds to capture frames
    FR: float
        Set frame rate as float datatype
    OUTPUT: str
        Output file name with format; ex: `output.avi`
    CODEC: str
        4-byte video codec (fourcc)
    """

    _change_dir()

    INIT_TIME = time.time()
    COUNTER = 0

    cap = cv2.VideoCapture(SOURCE)
    WIDTH, HEIGHT = int(cap.get(3)), int(cap.get(4))

    fourcc = cv2.VideoWriter_fourcc(*CODEC)
    out = cv2.VideoWriter(OUTPUT, fourcc, FR, (WIDTH, HEIGHT))

    while(cap.isOpened()):
        ret, frame = cap.read()
        # if `ret` TRUE --> frame is available
        if ret == True:
            out.write(frame)
            cv2.imshow(f'frame', frame)

            TIME = time.time()
            # capturing frames in between
            if TIME - INIT_TIME > CAPTURE_INTERVAL:
                cv2.imwrite(f"frame{COUNTER}.png", frame)
                INIT_TIME = TIME

            # waiting for 25 ms before capturing next frame
            if cv2.waitKey(WAIT_KEY) & 0xFF == ord('q'):
                break

            COUNTER += 1
        else:
            break

    cap.release()
    out.release()
    cv2.destroyAllWindows()

    return


def _change_dir():
    """Makes a new directory to store output video and frame.

    Directory name follows `output[\d]+` pattern. To avoid naming-clash int
    part of dir name is increased recursively until the dir name becomes unique
    in cwd.
    """

    dir_number = 0
    current_path = os.getcwd()
    while True:
        try:
            os.mkdir(current_path+f'/output{dir_number}')
            break
        except FileExistsError:
            dir_number += 1
    os.chdir(current_path+f'/output{dir_number}')

    return


if __name__ == "__main__":
    startapp()
