import tkinter as tk
from tkinter import Tk
from tkinter import *
from tkinter.filedialog import asksaveasfile
from tkinter import messagebox
from tkinter import filedialog
from itertools import product

txt = None
file_name = None
lst = []
words_list = "anal,anus,arse,ass,ass fuck,ass hole,assfucker,asshole,assshole,bastard,bitch,black cock,bloody hell,boong,cock,cockfucker,cocksuck,cocksucker,coon,coonnass,crap,cum,cunt,cyberfuck,damn,darn,dick,dirty,douche,dummy,erect,erection,erotic,escort,fag,faggot,fuck,Fuck off,fuck you,fuckass,fuckhole,god damn,gook,hard core,hardcore,hore,mother fucker,motherfuck,motherfucker,nigger,penisfucker,piss,piss off,pussy,retard,sadist,shit,slut,son of a bitch,tits,whore"
words_list = words_list.split(",")
swears = words_list

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
	global lst
	lst = []
	file_path = filedialog.askopenfilename(filetypes =[('.txt FILES', '*.txt')], title="Select a .txt file to censor")
	file_name = file_path
	txt_file = open(file_name, "r")
	txt = txt_file.read()

def add_to_lst(word):
	global lst
	lst.append(word)
	textBox.delete(1.0, END)

def swear():
	global swears
	global lst
	for i in swears:
		lst.append(i)

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
	new_file = asksaveasfile(defaultextension=".txt", title="SAVE FILE")
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

template = Label(root, bg="#1DACE8", justify=LEFT, text="\n\n\n\n")
template.pack()
myButton = Button(root, bg="#1DACE8", fg="#F24D29", text="QUIT", command=quit, cursor="hand1", borderwidth=2, relief="groove")
myButton.pack(expand=True, fill=BOTH)

root.mainloop()