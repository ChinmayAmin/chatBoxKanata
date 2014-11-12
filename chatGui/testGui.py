#will use Tkinter..just to try it
#!/usr/bin/python

from Tkinter import *

top = Tk()
top.width = 200
top.height = 200

#Creating simple chat box design...mind you i suck at graphics GG
name_label = Label(top,text="Your name")
name_label.pack( side = LEFT)
text_input = Entry(top,bd = 5)

text_input.pack(side = RIGHT)

top.mainloop()
