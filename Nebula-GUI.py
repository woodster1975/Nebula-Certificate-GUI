import sys
import os
import time
import pathlib
import tkinter as tk
from tkinter import *
import gui_support


def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    gui_support.init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    gui_support.init(w, top, *args, **kwargs)
    return (w, top)


class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = "wheat"  # X11 color: #999999
        _fgcolor = "#000000"  # X11 color: 'black'
        _compcolor = "#d9d9d9"  # X11 color: 'gray85'
        _ana1color = "#d9d9d9"  # X11 color: 'gray85'
        _ana2color = "#d9d9d9"  # X11 color: 'gray85'
        top.geometry("580x560+900+207")
        top.minsize(120, 1)
        top.maxsize(2100, 1061)
        top.resizable(1, 1)
        top.title("Nebula Cert Generator - V0.3 Python Tkinter")
        top.configure(relief="raised")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="#f5f5dedeb3b3")

        self.Button1 = tk.Button(top)
        # self.Button1.place(x=10, y=155, height=30, width=560)
        self.Button1.pack(padx=10, pady=170)
        self.Button1.configure(height=1, width=100)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(command=self.push_button)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(text="""Generate""")

        self.Label1 = tk.Label(top)
        self.Label1.place(x=200, y=10, height=21, width=38)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(cursor="fleur")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text="""Name""")

        self.Label1_4 = tk.Label(top)
        self.Label1_4.place(x=196, y=40, height=24, width=200)
        self.Label1_4.configure(activebackground="#f9f9f9")
        self.Label1_4.configure(activeforeground="black")
        self.Label1_4.configure(background="#d9d9d9")
        self.Label1_4.configure(disabledforeground="#a3a3a3")
        self.Label1_4.configure(foreground="#000000")
        self.Label1_4.configure(highlightbackground="#d9d9d9")
        self.Label1_4.configure(highlightcolor="black")
        self.Label1_4.configure(text="""IP Address / Mask eg 10.128.0.1/16 """)

        self.Label1_5 = tk.Label(top)
        self.Label1_5.place(x=188, y=70, height=24, width=200)
        self.Label1_5.configure(activebackground="#f9f9f9")
        self.Label1_5.configure(activeforeground="black")
        self.Label1_5.configure(background="#d9d9d9")
        self.Label1_5.configure(cursor="fleur")
        self.Label1_5.configure(disabledforeground="#a3a3a3")
        self.Label1_5.configure(foreground="#000000")
        self.Label1_5.configure(highlightbackground="#d9d9d9")
        self.Label1_5.configure(highlightcolor="black")
        self.Label1_5.configure(text="""Groups (seperated with comma)""")

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(x=196, y=100, height=24, width=148)
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text="""Duration (s,m,h - eg 10h)""")

        self.Label1_2 = tk.Label(top)
        self.Label1_2.place(x=197, y=128, height=24, width=57)
        self.Label1_2.configure(activebackground="#f9f9f9")
        self.Label1_2.configure(activeforeground="black")
        self.Label1_2.configure(background="#d9d9d9")
        self.Label1_2.configure(disabledforeground="#a3a3a3")
        self.Label1_2.configure(foreground="#000000")
        self.Label1_2.configure(highlightbackground="#d9d9d9")
        self.Label1_2.configure(highlightcolor="black")
        self.Label1_2.configure(text="""Subnets""")

        self.Text1 = tk.Text(top)
        self.Text1.place(x=10, y=210, height=340, width=545)
        self.Text1.configure(background="white")
        self.Text1.configure(cursor="fleur")
        self.Text1.configure(font="-family {Segoe UI} -size 9")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(wrap="word")
        instructions = read_instructions()
        if instructions:
            self.Text1.insert(tk.INSERT, (instructions + "\n"))
        self.scrollbar = Scrollbar(top)
        self.scrollbar.place(x=555, y=210, height=340)
        self.scrollbar.configure(command=self.Text1.yview)
        self.Text1.configure(yscrollcommand=self.scrollbar.set)
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(x=10, y=10, height=20, width=184)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="-family {Courier New} -size 10")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(highlightbackground="#d9d9d9")
        self.Entry1.configure(highlightcolor="black")
        self.Entry1.configure(insertbackground="black")
        self.Entry1.configure(selectbackground="#c4c4c4")
        self.Entry1.configure(selectforeground="black")

        self.Entry1_2 = tk.Entry(top)
        self.Entry1_2.place(x=10, y=40, height=20, width=184)
        self.Entry1_2.configure(background="white")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="-family {Courier New} -size 10")
        self.Entry1_2.configure(foreground="#000000")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="#c4c4c4")
        self.Entry1_2.configure(selectforeground="black")

        self.Entry1_3 = tk.Entry(top)
        self.Entry1_3.place(x=10, y=70, height=20, width=184)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_3.configure(font="-family {Courier New} -size 10")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(highlightbackground="#d9d9d9")
        self.Entry1_3.configure(highlightcolor="black")
        self.Entry1_3.configure(insertbackground="black")
        self.Entry1_3.configure(selectbackground="#c4c4c4")
        self.Entry1_3.configure(selectforeground="black")

        self.Entry1_4 = tk.Entry(top)
        self.Entry1_4.place(x=10, y=100, height=20, width=184)
        self.Entry1_4.configure(background="white")
        self.Entry1_4.configure(disabledforeground="#a3a3a3")
        self.Entry1_4.configure(font="-family {Courier New} -size 10")
        self.Entry1_4.configure(foreground="#000000")
        self.Entry1_4.configure(highlightbackground="#d9d9d9")
        self.Entry1_4.configure(highlightcolor="black")
        self.Entry1_4.configure(insertbackground="black")
        self.Entry1_4.configure(selectbackground="#c4c4c4")
        self.Entry1_4.configure(selectforeground="black")

        self.Entry1_5 = tk.Entry(top)
        self.Entry1_5.place(x=10, y=130, height=20, width=184)
        self.Entry1_5.configure(background="white")
        self.Entry1_5.configure(disabledforeground="#a3a3a3")
        self.Entry1_5.configure(font="-family {Courier New} -size 10")
        self.Entry1_5.configure(foreground="#000000")
        self.Entry1_5.configure(highlightbackground="#d9d9d9")
        self.Entry1_5.configure(highlightcolor="black")
        self.Entry1_5.configure(insertbackground="black")
        self.Entry1_5.configure(selectbackground="#c4c4c4")
        self.Entry1_5.configure(selectforeground="black")

        self.Checkbutton1 = tk.Checkbutton(top)
        self.Checkbutton1.place(x=350, y=10, height=25, width=161)
        self.Checkbutton1.configure(activebackground="#f4bcb2")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(cursor="fleur")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify="right")
        self.Checkbutton1.configure(text="""Generate Config""")
        self.check = IntVar()
        self.Checkbutton1.configure(onvalue=1)
        self.Checkbutton1.configure(offvalue=0)
        self.Checkbutton1.configure(variable=self.check)

    def push_button(self):
        name = self.Entry1.get()
        ip = self.Entry1_2.get()
        groups = self.Entry1_3.get()
        duration = self.Entry1_4.get()
        subnets = self.Entry1_5.get()
        check = self.check.get()
        if not name:
            self.Text1.delete(1.0, "end")
            self.Text1.insert(0.0, "Name & IP address required as a minimum")
            return
        if not ip:
            self.Text1.delete(1.0, "end")
            self.Text1.insert(0.0, "Name & IP address required as a minimum")
            return
        string = "nebula-cert.exe sign -name " + name + " -ip " + ip
        if groups:
            string = string + " -groups " + groups
        if duration:
            string = string + " -duration " + duration
        if subnets:
            string = string + " -subnets " + subnets
        self.Text1.delete(1.0, "end")
        self.Text1.insert(tk.INSERT, (str(string)) + "\n" + "\n")
        created = gui_support.create_cert(string, name)
        if not created:
            self.Text1.delete(1.0, "end")
            self.Text1.insert(0.0, "File already exists or other error")
            return
        else:
            out = gui_support.get_cert_details(name)
            self.Text1.insert(tk.INSERT, out)
            if check == 1:
                gui_support.config("ca.crt", name + ".crt", name + ".key", name)


def create_cert(string, name):
    created = False
    filename = name + ".crt"
    try:
        exists = check_exist(filename)
        if not exists:
            os.system(string)
            time.sleep(1)
            exists = check_exist(filename)
            if exists:
                created = True
            else:
                created = False
    except:
        created = False
    return created


def check_exist(filename):
    path = pathlib.Path(filename)
    exists = path.exists()
    return exists


def read_instructions():
    try:
        if os.path.exists("instructions.txt"):
            f = open("instructions.txt")
            instructions = f.read()
            f.close()
            return instructions
        else:
            instructions = None
            return instructions
    except:
        instructions = None
        return instructions


if __name__ == "__main__":
    vp_start_gui()
