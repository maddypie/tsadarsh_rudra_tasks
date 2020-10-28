import SpeechToText.SpeechToText as SpeechToText
import RockPaperScissor.RockPaperScissor as RockPaperScissor


def startapp():
    _welcome_screen()

    user_choice = int(input())
    choice = {
        1: lambda: SpeechToText.speech_to_text(),
        2: lambda: RockPaperScissor.start_game(),
        }
    callback = choice.get(user_choice, _wrong_input)
    output = callback()

    _output_screen(output)

    return


def _welcome_screen():
    print("Hit 1 for 'SpeechToText'")
    print("Hit 2 for Rock, Paper, Scissor game")
    return


def _wrong_input():
    msg = "Invalid input. Restart."
    return msg


def _output_screen(output: str):
    if output:
        print(output)


if __name__ == "__main__":
    startapp()
