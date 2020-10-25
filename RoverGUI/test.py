import tkinter as tk
from tkinter import ttk
from collections import namedtuple


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.event = namedtuple('event', ['keysym'])
        self.ON_OFF = tk.StringVar()
        self.ON_OFF.set("OFF")
        self.AUTO = tk.StringVar()
        self.AUTO.set("MANUAL")
        self.BATTERY = tk.IntVar()
        self.BATTERY.set(75)
        self.SPEED = tk.StringVar()
        self.SPEED.set('0')
        self.LOG_ENTRY = ["rover initiated..."]
        self.LOG = tk.StringVar(value=self.LOG_ENTRY)
        self.make_window()

    def make_window(self):
        mainframe = ttk.Frame(self)
        self.make_on_off(mainframe)
        self.make_auto(mainframe)
        self.make_rudra_label(mainframe)
        self.make_battery(mainframe)
        self.make_speed(mainframe)
        self.make_log_screen(mainframe)
        self.key_binding()
        mainframe.grid()

    def make_on_off(self, root):
        on_off = ttk.Frame(root)
        on_off_button = ttk.Button(on_off, textvariable=self.ON_OFF,
                                   command=self.switch_on_off)
        on_off.grid(row=0, rowspan=2, column=2)
        on_off_button.grid(padx=1, pady=2)

    def switch_on_off(self):
        status = self.ON_OFF.get()
        if status == 'OFF':
            event = self.event('ROVER ON')
            self.ON_OFF.set('ON')
        else:
            event = self.event('ROVER OFF')
            self.ON_OFF.set('OFF')
        self._callback(event)

    def make_auto(self, root):
        auto = ttk.Frame(root)
        auto_button = ttk.Button(auto, textvariable=self.AUTO,
                                 command=self.switch_auto)
        auto.grid(row=0, rowspan=2, column=1)
        auto_button.grid(padx=1, pady=2)

    def switch_auto(self):
        status = self.AUTO.get()
        if status == "MANUAL":
            event = self.event("MODE MANUAL")
            self.AUTO.set("AUTO")
        else:
            event = self.event("MODE AUTO")
            self.AUTO.set("MANUAL")
        self._callback(event)

    def make_rudra_label(self, root):
        rudra_label = ttk.Label(root, text='rudra',
                                width=12, anchor='center')
        rudra_label.grid(row=0, column=0)

    def make_battery(self, root):
        battery = ttk.Frame(root)
        battery_bar = ttk.Progressbar(battery, variable=self.BATTERY,
                                      mode='determinate', orient='horizontal')
        battery.grid(row=2, column=1, columnspan=2)
        battery_bar.grid(padx=2, pady=2)

    def make_speed(self, root):
        speed = ttk.Frame(root)
        speed_val = ttk.Label(speed, textvariable=self.SPEED)
        speed.grid(row=3, rowspan=2, column=1, columnspan=2)
        speed_val.grid()

    def make_log_screen(self, root):
        log_window = ttk.Frame(root)
        log_screen = tk.Listbox(log_window, listvariable=self.LOG)
        log_window.grid(row=2, rowspan=4, column=0)
        log_screen.grid(padx=2, pady=2)

    def key_binding(self):
        self.bind("<Key>", self._callback)

    def _callback(self, event):
        update = [f"COMMAND: {event.keysym}"]
        self.LOG_ENTRY.insert(0, update)
        self.LOG.set(self.LOG_ENTRY)


if __name__ == "__main__":
    instance = App()
    instance.mainloop()
