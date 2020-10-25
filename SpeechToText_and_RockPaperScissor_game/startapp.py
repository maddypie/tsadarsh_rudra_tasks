import tkinter as tk
from tkinter import ttk

import SpeechToText.SpeechToText as SpeechToText
import RockPaperScissor.RockPaperScissor as RockPaperScissor

root = tk.Tk()
root.title('Speechy')

mainframe = ttk.Frame(root)
label_frame = ttk.Frame(mainframe, relief='sunken')

label_display = tk.StringVar()
label_display.set('Ready')
label = ttk.Label(label_frame, textvariable=label_display, width=20, anchor='center', wraplength=8*20, justify='left')


def callback():
    global label
    choice = option.get()
    label_display.set('Listening...')
    if choice == 0:
        text = SpeechToText.speech_to_text()
    if choice == 1:
        text = RockPaperScissor.start_game()
    label_display.set(text)


option = tk.IntVar()
option.set(-1)
op1 = ttk.Radiobutton(mainframe, text='Speech To Text', command=callback,
                      variable=option, value=0)
op2 = ttk.Radiobutton(mainframe, text='Rock Paper Scissors', command=callback,
                      variable=option, value=1)

mainframe.grid(sticky='nsew')
op1.grid(row=0, column=0, padx=5, pady=3)
op2.grid(row=1, column=0, padx=5, pady=3)
label_frame.grid(row=2, column=0, padx=3, pady=3, sticky='nsew')
label.grid(row=2, column=0, padx=5, pady=3, sticky='nsew')

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(2, weight=1)

root.mainloop()
