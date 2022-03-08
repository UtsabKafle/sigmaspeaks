import tkinter as tk
from tkinter import Label, ttk,scrolledtext,Text
from tkinter.constants import END
import pyttsx3

def convert():
    engine = pyttsx3.init()
    engine.say("Process started")
    engine.save_to_file(str(scr.get(1.0,END)), str(text.get()+".mp3"))
    engine.runAndWait()
def clear():
    scr.delete(1.0,END)
win = tk.Tk()
win.title("Sigma Speaks")
text = tk.StringVar()
ttk.Label(win,text="Sigma Speaks").grid(column=0,row=0,padx=(10,10),pady=(10,10),columnspan=2)
scr = Text(win,width=40,height=15,wrap=tk.WORD)
scr.grid(column=0,row=1,padx=(10, 10),pady=(10,10),columnspan=2)
ttk.Label(text="File Name").grid(row=2,column=0)
text_inp = ttk.Entry(win,width=25,textvariable=text).grid(column=1,row=2,padx=(10,10),pady=(5,5))
button = ttk.Button(win,text="Create",command=convert).grid(column=0,row=3,padx=(10,10),pady=(5,5))
button = ttk.Button(win,text="Clear",command=clear).grid(column=1,row=3,padx=(10,10),pady=(5,5))
win.mainloop()