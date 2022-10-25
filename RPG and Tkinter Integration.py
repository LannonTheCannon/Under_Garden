# RPG Game Integrated Tkinter Chat Bot

# Include your libraries
from tkinter import *
import tkinter.messagebox
from tkinter import ttk
import random
import time
import datetime
import asciiart


root = Tk()

# create class
class Window1:

    def __init__(self, master):
        
        self.master = master
        self.master.title('Creative Core Management System')
        self.master.geometry('620x460+0+0')
        self.master.config(bg = 'slategray4')
        self.frame = Frame(self.master, bg = 'slategray4')
        self.frame.pack()

        # Add key players here
        self.query = StringVar() 

        #Create Frames
        self.mainFrame = Frame(self.frame, bg = 'gray50', width = 620, height = 460,
                               relief = SUNKEN, bd = 8)
        self.mainFrame.pack()

        # Create the upper frame
        self.topFrame = Frame(self.mainFrame, bg = 'gray40', width = 620, height = 400,
                              relief = RAISED, bd = 8)
        self.topFrame.pack(side = TOP)
        self.topFrame.pack_propagate(0)

        # Create the lower frame
        self.lowerFrame = Frame(self.mainFrame, bg = 'gray40', width = 620, height = 60,
                              relief = RAISED, bd = 8)
        self.lowerFrame.pack(side = BOTTOM)
        self.lowerFrame.pack_propagate(0)

        #### Add Widgets ###########################################################
        self.test = '''
 █    ██  ███▄    █ ▓█████▄ ▓█████  ██▀███  
 ██  ▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▓██  ▒██░▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
▓▓█  ░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
▒▒█████▓ ▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░░▒░ ░ ░ ░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ░░░ ░ ░    ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
   ░              ░    ░       ░  ░   ░     
                     ░
  ▄████  ▄▄▄       ██▀███  ▓█████▄ ▓█████  ███▄    █ 
 ██▒ ▀█▒▒████▄    ▓██ ▒ ██▒▒██▀ ██▌▓█   ▀  ██ ▀█   █ 
▒██░▄▄▄░▒██  ▀█▄  ▓██ ░▄█ ▒░██   █▌▒███   ▓██  ▀█ ██▒
░▓█  ██▓░██▄▄▄▄██ ▒██▀▀█▄  ░▓█▄   ▌▒▓█  ▄ ▓██▒  ▐▌██▒
░▒▓███▀▒ ▓█   ▓██▒░██▓ ▒██▒░▒████▓ ░▒████▒▒██░   ▓██░
 ░▒   ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░ ▒▒▓  ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
  ░   ░   ▒   ▒▒ ░  ░▒ ░ ▒░ ░ ▒  ▒  ░ ░  ░░ ░░   ░ ▒░
░ ░   ░   ░   ▒     ░░   ░  ░ ░  ░    ░      ░   ░ ░ 
      ░       ░  ░   ░        ░       ░  ░         ░
                      
'''
        self.test2 = '-- Press Enter to Start -- '

        self.outputBox = Label(self.topFrame, bg = 'antiquewhite2', width = 130,
                               height = 30, text = '', font = 'courier 5 bold',
                               wraplength = 600)
        self.outputBox.pack(side = TOP, fill = BOTH, expand = True)
        

        self.inputBox = Entry(self.lowerFrame, bg = 'ghostwhite', width = 42,
                                text = '', textvariable = self.query, font = 'terminal 12 ',
                              relief = SUNKEN)
        self.inputBox.pack(side = LEFT)

        self.btnSend = Button(self.lowerFrame, width = 7, height = 3 ,text = 'ENTER',
                              command = self.send, bg = 'indianred', font = 'terminal 12')
        self.btnSend.pack(side = RIGHT)

        self.intro = '''

    RPG Game
    ++++++++

        Get to the Garden with a key and a potion
        Avoid the monsters!

        Commands:
        go [direction]
        get [item]
'''


    def send(self):
        # use the self.query variable
        newQuery = self.query.get().lower().split()

        if newQuery[0] == 'start' and newQuery[1] == 'game':
            self.print_intro(self.test)
            self.btnSend.configure(command = self.start_game)

    def start_game(self):
        self.print_general(self.intro) 
        self.outputBox.configure(text = 'ITS WORKING')
          
    def waithere(self):
        var = IntVar()
        root.after(1, var.set, 1)
        root.wait_variable(var)

    def waithere2(self):
        var = IntVar()
        root.after(50, var.set, 1)
        root.wait_variable(var)

    def print_intro(self, message):
        self.outputBox.configure(font = 'system 10 bold', width = 81, height = 18)
        string_output = ''
        for char in message:
            string_output += char
            self.outputBox.configure(text = string_output, font = 'terminal 8 bold',
                                     wraplength = 600, justify = CENTER)
            self.waithere()
        self.query.set('')

    def print_general(self, message):
        self.outputBox.configure(font = 'system 10 bold', width = 81, height = 18)
        string_output = ''
        for char in message:
            string_output += char
            self.outputBox.configure(text = string_output, font = 'terminal 12 bold',
                                     wraplength = 600, justify = CENTER)
            self.waithere2()
        self.query.set('')

        

app = Window1(root)
root.mainloop() 
