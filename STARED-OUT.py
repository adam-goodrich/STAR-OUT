import tkinter as tk
from tkinter import Tk
from tkinter import *
from tkinter.filedialog import askdirectory
from tkinter import messagebox
from tkinter import filedialog
from itertools import product
import ntpath
import os

txt = None
file_name = None

root = Tk()
root.title("STARED-OUT")
root.configure(background='#1DACE8')
width, height = root.winfo_screenwidth() / 3, root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width,height))
template = Label(root, bg="#1DACE8",  justify=CENTER, text=""" """)
template.pack()

def open_file():
	global file_name
	global txt
	file_path = filedialog.askopenfilename(filetypes =[('.txt FILES', '*.txt')], title="Select a .txt file to censor")
	file_name = file_path
	txt_file = open(file_name, "r")
	txt = txt_file.read()

swears = ["tits", "cocksucker", "piss", "Fuck", "Shit", "Prick", "Bastard", "Bellend", "Cunt", "Balls", "Bitch", "Pussy"]
lst = []

def add_to_lst(word):
	global lst
	lst.append(word)
	textBox.delete(1.0, END)

def swear():
	global swears
	global lst
	for i in swears:
		lst.append(i)

def choose_directory():
    '''This changes the working directory to the directory of your choice'''
    tk.messagebox.showinfo(title="CHOOSE DIRECTORY", message="Click 'OK' and choose the directory you want to save your new censored file in")
    directory = askdirectory()
    os.chdir(directory)

def censor_string(txt, lst):
	l = []
	for i in lst:
		word = [(c, c.upper()) if not c.isdigit() else (c,) for c in i.lower()]
		all_word = ["".join(item) for item in product(*word)]
		for j in all_word:
			l.append(j)
	index = 0
	while index < len(l):
		txt = txt.replace(l[index], (len(l[index]) * "*"))
		index += 1
	choose_directory()
	new_file = open(f"censored_{ntpath.basename(file_name)}","w+")
	new_file.write(txt)


def quit():
    try:
        sys.exit()
    except:
        sys.exit()

myButton = Button(root, bg="#1DACE8", fg="#F24D29", text="OPEN FILE", command=open_file, cursor="hand1", borderwidth=2, relief="groove")
myButton.pack(expand=True, fill=BOTH)

template = Label(root, bg="#1DACE8",  justify=CENTER, text="""\nCLICK THE BUTTON BELOW TO ADD COMMON SWEAR WORDS (optional)\n""")
template.pack()
myButton = Button(root, bg="#1DACE8", fg="#F24D29", text="ADD COMMON SWEAR WORDS (optional)", command= lambda: swear(), cursor="hand1", borderwidth=2, relief="groove")
myButton.pack(expand=True, fill=BOTH)

template = Label(root, bg="#1DACE8", justify=CENTER, text="""
If you need to censor a word that is not a common swear 
enter it in the box below and press the add word button
You can enter as many words as you want""")
template.pack()
textBox=Text(root, bg="#C4CFD0", fg="#F24D29", height=6, width=60, relief="sunken")
textBox.pack()

template = Label(root, bg="#1DACE8", justify=CENTER, text=""" """)
template.pack()
myButton = Button(root, bg="#1DACE8", fg="#F24D29", text="ADD CUSTOM WORD", command=lambda: add_to_lst(textBox.get("1.0","end-1c")), cursor="hand1", relief="groove")
myButton.pack(expand=True, fill=BOTH)

template = Label(root, bg="#1DACE8",  justify=CENTER, text="""\nPress the button below to STAR-OUT the bad words\n""")
template.pack()
censor_string_button = Button(root, bg="#1DACE8", fg="#F24D29", text="STAR-OUT", command= lambda: censor_string(txt, lst), cursor="hand1").pack(expand=True, fill=BOTH)

template = Label(root, bg="#1DACE8", justify=LEFT, text="\n\n\n\n\n\n")
template.pack()
myButton = Button(root, bg="#1DACE8", fg="#F24D29", text="QUIT", command=quit, cursor="hand1", borderwidth=2, relief="groove")
myButton.pack(expand=True, fill=BOTH)

root.mainloop()



