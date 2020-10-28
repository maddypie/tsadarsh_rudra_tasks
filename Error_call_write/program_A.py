import time


def write_exception(exception):
    """Content provided is appeneded to `log.txt`"""

    with open('log.txt', 'a') as file:
        log = f"{time.asctime()} {exception}\n"
        file.write(log)

