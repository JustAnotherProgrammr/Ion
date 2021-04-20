import os
import base64
import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from ttkthemes import ThemedTk

class Main:
    def __init__(self):
        self.root = ThemedTk(theme="scidblue")
        self.root.geometry("1000x995")
        self.root.title("Ion - Untitled.txt")
        self.data = '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'
        self.img = PhotoImage(data=self.data)
        self.root.tk.call("wm", "iconphoto", self.root._w, self.img)
        self.root.tk.call()
        self.FILENAME = "Untitled.txt"
        self.FRAME = ttk.Frame()
        self.FRAME.pack(anchor="w")
        def NEWFILE():
            global FILENAME
            self.FILENAME = "Untitled.txt"
            self.root.title("Ion - Untitled.txt")
            self.TEXT_INPUT.delete(0.0, END)
        self.BTN1 = ttk.Button(self.FRAME, text="New File", command=NEWFILE)
        self.BTN1.pack(side=LEFT)
        #self.BTN1.place(x=1)
        def SAVEAS(*args):
            try:
                self.WRITEFILE = filedialog.asksaveasfile()
                self.TEXT = self.TEXT_INPUT.get(0.0, END)
                global FILENAME
                self.FILEPATH = self.WRITEFILE.name
                self.FILENAME = os.path.split(str(self.FILEPATH))[1]
                print(self.FILENAME)
                self.root.title("Ion - " + self.FILENAME)
                self.WRITEFILE.write(self.TEXT)
                self.WRITEFILE.close()
            except (TypeError, AttributeError) as NOTWORKING:
                pass
        self.BTN2 = ttk.Button(self.FRAME, text="Save As", command=SAVEAS)
        self.BTN2.pack(side=LEFT)
        #self.BTN2.place(x=58)
        def SAVEFILE(*args):
            self.TEXT = self.TEXT_INPUT.get(0.0, END)
            global FILENAME
            self.WRITEFILE = open(self.FILENAME, "w")
            if self.FILENAME == "Untitled.txt":
                os.remove("Untitled.txt")
                SAVEAS()
            else:
                self.WRITEFILE.write(self.TEXT)
                self.WRITEFILE.close()
        self.BTN3 = ttk.Button(self.FRAME, text="Save", command=SAVEFILE)
        self.BTN3.pack(side=LEFT)
        #self.BTN3.place(x=110)
        def OPENFILE():
            try:
                self.WRITEFILE = open(filedialog.askopenfilename(), "r")
                self.TEXT = self.WRITEFILE.read()
                self.TEXT_INPUT.delete(0.0, END)
                self.TEXT_INPUT.insert(0.0, self.TEXT)
                self.FILEPATH = self.WRITEFILE.name
                self.FILENAME = os.path.split(str(self.FILEPATH))[1]
                print(self.FILENAME)
                self.root.title("Ion - " + self.FILENAME)
            except (TypeError, FileNotFoundError) as NOTWORKING:
                pass
        self.BTN4 = ttk.Button(self.FRAME, text="Open", command=OPENFILE)
        self.BTN4.pack(side=LEFT)
        #self.BTN4.place(x=146)
        self.SCRLBR = ttk.Scrollbar(self.root)
        self.SCRLBR.pack(side=RIGHT, fill=Y)
        self.TEXT_INPUT = Text(self.root, yscrollcommand=self.SCRLBR.set)
        self.TEXT_INPUT.pack(fill=BOTH, expand=True)
        self.SCRLBR.config(command=self.TEXT_INPUT.yview)
        def select_all(*args):
            self.TEXT_INPUT.tag_add(SEL, "1.0", END)
            return "break"
        self.TEXT_INPUT.bind("<Control-Key-a>", select_all)
        self.TEXT_INPUT.bind("<Control-Key-A>", select_all)
        self.TEXT_INPUT.bind("<Control-Key-s>", SAVEFILE)
        self.TEXT_INPUT.bind("<Control-Key-S>", SAVEAS)
        self.root.mainloop()

Main()
