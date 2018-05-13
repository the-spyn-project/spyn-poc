####################################################################################################
# Overview: THIS MODULE CONTAINS THE MAIN GUI
# Created on April 22, 2018
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
        self.initialize_seller_frame()

    def initialize_gui(self):

        self.gui_w = 900
        self.gui_h = 600

        self.seller_frame_h = 200
        self.seller_frame_w = 300
        self.seller_frame_x = 3
        self.seller_frame_y = 3

        self.sample_btn_h = 25
        self.sample_btn_w = 150
        self.sample_btn_x = 5
        self.sample_btn_y = 5

        self.gui = tk.Tk()
        self.gui.resizable(width=False,height=False)
        self.gui.geometry('{}x{}'.format(self.gui_w,self.gui_h))
        self.gui.title('SPYN')
        #self.gui.iconbitmap(r'C:\Users\Veda Sadhak\Desktop\GIT\spyn-poc\images\logo.ico')

    def initialize_seller_frame(self):

        seller_frame_container = tk.Frame(self.gui)
        seller_frame_container.place(height=self.seller_frame_h+2,
                           width=self.seller_frame_w+2,
                           x=self.seller_frame_x,
                           y=self.seller_frame_y)

        seller_frame = tk.LabelFrame(seller_frame_container,text='Seller')
        seller_frame.place(height=self.seller_frame_h,
                           width=self.seller_frame_w,
                           x=self.seller_frame_x,
                           y=self.seller_frame_y)

        sample_btn = tk.Button(seller_frame,
                               text='Sample Button',
                               font='Arial 8',
                               command=lambda:self.sample_function())
        sample_btn.place(height=self.sample_btn_h,
                         width=self.sample_btn_w,
                         x=self.sample_btn_x,
                         y=self.sample_btn_y)

    def sample_function(self):

        logger.info("This is a sample function")

    def run(self):

        self.gui.mainloop()


# MAIN
# ==================================================================================================

if __name__ == '__main__':

    spyn_app = spyn()
    spyn_app.run()