import tkinter as tk
from tkinter import ttk
from collections import namedtuple


class App(tk.Tk):

    def __init__(self):
        super().__init__()
        self.styler = ttk.Style()
        self.styler.theme_use('clam')
        self.event = namedtuple('event', ['keysym'])
        self.ON_OFF = tk.StringVar(value="OFF")
        self.AUTO = tk.StringVar(value="MANUAL")
        self.HEADING = tk.StringVar(value='rudra')
        self.BATTERY = tk.IntVar(value=75)
        self.SPEED = tk.StringVar(value='0.0\nkm/h')
        self.LOG_ENTRY = ["rover initiated..."]
        self.LOG = tk.StringVar(value=self.LOG_ENTRY)
        self.X_CORD = tk.StringVar(value='X: 100.0')
        self.Y_CORD = tk.StringVar(value='Y: 100.0')
        self.make_window()
        self.key_binding()

    def make_window(self):
        mainframe = ttk.Frame(self)
        self.make_on_off(mainframe)
        self.make_auto(mainframe)
        self.make_rudra_label(mainframe)
        self.make_battery(mainframe)
        self.make_speed(mainframe)
        self.make_log_screen(mainframe)
        self.make_x_cord(mainframe)
        self.make_y_cord(mainframe)

        mainframe.grid(sticky='nsew')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        for r in range(4):
            mainframe.rowconfigure(r, weight=1)
        for r in range(3, 5):
            mainframe.rowconfigure(r, weight=3)
        for c in range(3):
            mainframe.columnconfigure(c, weight=1)

    def make_on_off(self, root):
        on_off_button = ttk.Button(root, textvariable=self.ON_OFF,
                                   command=self.switch_on_off)
        on_off_button.grid(row=0, rowspan=2, column=2,
                           padx=1, pady=2, sticky='nsew')

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
        auto_button = ttk.Button(root, textvariable=self.AUTO,
                                 command=self.switch_auto)
        auto_button.grid(row=0, rowspan=2, column=1,
                         padx=1, pady=2, sticky='nsew')

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
        rudra_label = ttk.Label(root, text=self.HEADING.get(),
                                anchor='center')
        rudra_label.grid(row=0, column=0, sticky='nsew')

    def make_battery(self, root):
        battery_bar = ttk.Progressbar(root, variable=self.BATTERY,
                                      mode='determinate', orient='horizontal')
        battery_bar.grid(row=2, column=1, columnspan=2,
                         padx=2, pady=2, sticky='nsew')

    def make_speed(self, root):
        speed_val = ttk.Label(root, textvariable=self.SPEED,
                              anchor='center', justify='center')
        speed_val.grid(row=3, rowspan=2, column=2,
                       padx=2, pady=2, sticky='nsew')

    def make_log_screen(self, root):
        log_screen = tk.Listbox(root, listvariable=self.LOG)
        log_screen.grid(row=2, rowspan=4, column=0,
                        padx=2, pady=2, sticky='nsew')

    def make_x_cord(self, root):
        x_cord = ttk.Label(root, textvariable=self.X_CORD,
                           anchor='center', relief='sunken')
        x_cord.grid(row=3, column=1, sticky='nsew')

    def make_y_cord(self, root):
        y_cord = ttk.Label(root, textvariable=self.Y_CORD,
                           anchor='center', relief='sunken')
        y_cord.grid(row=4, column=1, sticky='nsew')

    def key_binding(self):
        self.bind("<Key>", self._callback)

    def _callback(self, event):
        keysym = event.keysym
        update = [f"COMMAND: {keysym}"]
        self.LOG_ENTRY.insert(0, update)
        self.LOG.set(self.LOG_ENTRY)


if __name__ == "__main__":
    instance = App()
    instance.mainloop()