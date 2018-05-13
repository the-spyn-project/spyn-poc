####################################################################################################
# Overview: THIS MODULE CONTAINS THE MAIN GUI
# Created on May 5th, 2018
####################################################################################################


# GLOBAL IMPORTS
# ==================================================================================================

import os
import sys
import tkinter as tk


# LOCAL IMPORTS
# ==================================================================================================

cwd = os.getcwd()
parent_dir = os.path.abspath(os.path.join(cwd,os.pardir))
core_path = parent_dir + r'\core'
sys.path.append(core_path)

from logger import *


# GUI CLASS
# ==================================================================================================

class spyn:

    def __init__(self):

        self.initialize_gui()
        self.initialize_tab_buttons()
        self.initialize_provider_frame()
        self.initialize_commander_frame()
        self.initialize_account_frame()

    def initialize_gui(self):

        self.gui_w = 1500
        self.gui_h = 800

        self.tab_btn_h = 25
        self.tab_btn_w = 150
        self.tab_btn_x = 20
        self.tab_btn_y = 20

        self.tab_container_h = self.gui_h - (self.tab_btn_y + self.tab_btn_h) - self.tab_btn_x
        self.tab_container_w = 700
        self.tab_container_x = self.tab_btn_x + 1  # 1 offset is required to be aligned
        self.tab_container_y = self.tab_btn_y + self.tab_btn_h
        self.container_offset = 2

        self.sample_btn_h = 30
        self.sample_btn_w = 150
        self.sample_btn_x = 5
        self.sample_btn_y = 5

        self.gui = tk.Tk()
        self.gui.resizable(width=False,height=False)
        self.gui.geometry('{}x{}'.format(self.gui_w,self.gui_h))
        self.gui.title('SPYN')
        self.gui.iconbitmap(r'C:\Users\Veda Sadhak\Desktop\GIT\spyn-poc\images\logo.ico')

    def initialize_tab_buttons(self):

        provider_btn = tk.Button(self.gui,
                                 text='Provider',
                                 font='Arial 8',
                                 command=lambda: self.toggle_tabs('provider'))
        provider_btn.place(height=self.tab_btn_h,
                           width=self.tab_btn_w,
                           x=self.tab_btn_x,
                           y=self.tab_btn_y)

        commander_btn = tk.Button(self.gui,
                                 text='Commander',
                                 font='Arial 8',
                                 command=lambda: self.toggle_tabs('commander'))
        commander_btn.place(height=self.tab_btn_h,
                            width=self.tab_btn_w,
                            x=self.tab_btn_x+self.tab_btn_w,
                            y=self.tab_btn_y)

        account_btn = tk.Button(self.gui,
                                 text='Account',
                                 font='Arial 8',
                                 command=lambda: self.toggle_tabs('account'))
        account_btn.place(height=self.tab_btn_h,
                          width=self.tab_btn_w,
                          x=self.tab_btn_x+self.tab_btn_w*2,
                          y=self.tab_btn_y)

    def initialize_provider_frame(self):

        self.provider_frame_container = tk.Frame(self.gui)
        self.provider_frame_container.place(height=self.tab_container_h+self.container_offset,
                                            width=self.tab_container_w+self.container_offset,
                                            x=self.tab_container_x,
                                            y=self.tab_container_y)

        provider_frame = tk.LabelFrame(self.provider_frame_container,text='')
        provider_frame.place(height=self.tab_container_h,
                             width=self.tab_container_w,
                             x=0,
                             y=0)

        sample_btn = tk.Button(provider_frame,
                               text='Sample Button 1',
                               font='Arial 8',
                               command=lambda:self.sample_function())

        sample_btn.place(height=self.sample_btn_h,
                         width=self.sample_btn_w,
                         x=self.sample_btn_x,
                         y=self.sample_btn_y)

    def initialize_commander_frame(self):

        self.commander_frame_container = tk.Frame(self.gui)
        self.commander_frame_container.place(height=self.tab_container_h+self.container_offset,
                                             width=self.tab_container_w+self.container_offset,
                                             x=self.tab_container_x,
                                             y=self.tab_container_y)

        commander_frame = tk.LabelFrame(self.commander_frame_container,text='')
        commander_frame.place(height=self.tab_container_h,
                              width=self.tab_container_w,
                              x=0,
                              y=0)

        sample_btn = tk.Button(commander_frame,
                               text='Sample Button 2',
                               font='Arial 8',
                               command=lambda:self.sample_function())

        sample_btn.place(height=self.sample_btn_h,
                         width=self.sample_btn_w,
                         x=self.sample_btn_x,
                         y=self.sample_btn_y)

    def initialize_account_frame(self):

        self.account_frame_container = tk.Frame(self.gui)
        self.account_frame_container.place(
            height=self.tab_container_h + self.container_offset,
            width=self.tab_container_w + self.container_offset,
            x=self.tab_container_x,
            y=self.tab_container_y)

        account_frame = tk.LabelFrame(self.account_frame_container, text='')
        account_frame.place(height=self.tab_container_h,
                              width=self.tab_container_w,
                              x=0,
                              y=0)

        sample_btn = tk.Button(account_frame,
                               text='Sample Button 3',
                               font='Arial 8',
                               command=lambda: self.sample_function())

        sample_btn.place(height=self.sample_btn_h,
                         width=self.sample_btn_w,
                         x=self.sample_btn_x,
                         y=self.sample_btn_y)

    def toggle_tabs(self,tab):

        if tab == 'provider':
            self.commander_frame_container.place_forget()
            self.account_frame_container.place_forget()
            self.provider_frame_container.place(height=self.tab_container_h+self.container_offset,
                                                width=self.tab_container_w+self.container_offset,
                                                x=self.tab_container_x,
                                                y=self.tab_container_y)
            logger.info("Provider frame is now viewable")

        elif tab == 'commander':
            self.provider_frame_container.place_forget()
            self.account_frame_container.place_forget()
            self.commander_frame_container.place(height=self.tab_container_h+self.container_offset,
                                                 width=self.tab_container_w+self.container_offset,
                                                 x=self.tab_container_x,
                                                 y=self.tab_container_y)
            logger.info("Commander frame is now viewable")

        elif tab == 'account':
            self.provider_frame_container.place_forget()
            self.commander_frame_container.place_forget()
            self.account_frame_container.place(height=self.tab_container_h + self.container_offset,
                                               width=self.tab_container_w + self.container_offset,
                                               x=self.tab_container_x,
                                               y=self.tab_container_y)
            logger.info("Account frame is now viewable")

    def sample_function(self):

        logger.info("This is a sample function")

    def run(self):

        self.gui.mainloop()


# MAIN
# ==================================================================================================

if __name__ == '__main__':

    spyn_app = spyn()
    spyn_app.run()