"""
##### Task 1
Create a "Madlib" that has the users enter in a variety of noun/verb/adjectives.
When they press a button, it should update the contents of a label to display
the completed madlib.
What is a madlib? Visit https://www.madlibs.com/printables/ to see some Madlibs
you might use in your assignment
"""
import tkinter as tk
from tkinter import * 

window = tk.Tk()

eoutput = StringVar()
eoutput.set("Output goes here")

def clickFunction():
    word = e1.get()
    word2 = e2.get()
    word3 = e3.get()
    word4 = e4.get()
    word5 = e5.get()
    a_entry.delete(0,END)
    a_entry.insert(0,"Dear " + word + ", " + word2 + "  are red, " + word3 + " are blue, You love me and I love " + word4 + "! From " + word5 + ".")

l1 = Label(window, text="Dear ")
e1 = Entry(window)
l2 = Label(window, text=",")
e2 = Entry(window)
l3 = Label(window, text=" are red, ")
e3 = Entry(window)
l4 = Label(window, text=" are blue, You love me and I love ")
e4 = Entry(window)
l5 = Label(window, text="! From ")
e5 = Entry(window)
l6 = Label(window, text=".")
b1 = Button(window, text="Click to see output", command=clickFunction)
a_entry = Entry(window, width=70, textvariable=eoutput)

l1.pack()
e1.pack()
l2.pack()
e2.pack()
l3.pack()
e3.pack()
l4.pack()
e4.pack()
l5.pack()
e5.pack()
l6.pack()
b1.pack()
a_entry.pack()
window.mainloop()
