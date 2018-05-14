#test.py
import tkinter as tk  # for python 3
from tkinter import messagebox

import pygubu

# define the function callbacks
def on_button1_click():
    messagebox.showinfo('Message', 'You clicked Button 1')

class Application:
    def __init__(self):

        #1: Create a builder
        self.builder = builder = pygubu.Builder()

        #2: Load an ui file
        builder.add_from_file('spyn_ui.ui')

        #3: Create the widget using a master as parent
        self.mainwindow = builder.get_object('toplevel_gui')
        self.mainwindow.protocol("WM_DELETE_WINDOW", self.on_close_window)

        callbacks = {
            'on_add_device_button_clicked': on_button1_click
        }

        builder.connect_callbacks(callbacks)

    def on_close_window(self, event=None):
        print('On close window')

        # Call destroy on toplevel to finish program
        self.mainwindow.destroy()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':

    app = Application()
    app.run()
