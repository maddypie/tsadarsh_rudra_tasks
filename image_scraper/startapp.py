import tkinter as tk
from tkinter import ttk
import os

from main import startapp


def search():
    global item, spinval
    global hint
    save_path = startapp(item.get(), spinval.get())
    hint.set(save_path)


root = tk.Tk()
root.title('HQPicturer')

item = tk.StringVar()
spinval = tk.IntVar()
spinval.set(10)
hint = tk.StringVar()
hint.set(os.getcwd())

mainframe = ttk.Frame(root)

label1 = ttk.Label(mainframe, text='Looking for')
keyword = ttk.Entry(mainframe, textvariable=item)
num = tk.Spinbox(mainframe, from_=1, to=100, textvariable=spinval,
                 wrap=True, width=5)
go = ttk.Button(mainframe, text='Go', command=search)
hinter = ttk.Label(mainframe, textvariable=hint)

mainframe.grid()
label1.grid(row=1, column=1, padx=3, pady=3, sticky='nsew')
keyword.grid(row=1, column=2, sticky='nsew')
num.grid(row=1, column=3, padx=3, pady=3)
go.grid(row=1, column=4, padx=3, pady=3)
hinter.grid(row=2, column=1, padx=3, pady=3, columnspan=4)


root.mainloop()
