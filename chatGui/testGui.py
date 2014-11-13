#will use Tkinter..just to try it
#!/usr/bin/python

try:
	from Tkinter import *
except ImportError:
	from tkinter import *

#create the main window
root = Tk()
root.resizable(width = FALSE, height = FALSE)

#Creating simple chat box design...mind you i suck at graphics GG
#Create main text area. Use a frame of root
textPad = Frame(root)
textPad.pack()

#Create the bottom text input and name area
textInput = Frame(root)

#Set the area for the top input area
textArea = Text(textPad,width = 60,height = 20)

#Add the scrollbar and attach to textArea
scroll = Scrollbar(textPad)
textArea.configure(yscrollcommand = scroll.set)
textArea.configure(state = DISABLED)

#Pack em all
textArea.pack(side = LEFT, fill = BOTH)
scroll.pack(side = RIGHT, fill = BOTH)
textPad.pack(side = TOP, fill = BOTH)

#Set the area for the bottom inputs
name_label = Label(textInput, text = "Your name")
text_input = Entry(textInput, width = 40)

#pack em all
name_label.pack(side = LEFT,fill = BOTH) 
text_input.pack(side = RIGHT,fill = BOTH)
textInput.pack(side = BOTTOM, fill = BOTH)

#Main loop meaning until user pressed close
root.mainloop()
