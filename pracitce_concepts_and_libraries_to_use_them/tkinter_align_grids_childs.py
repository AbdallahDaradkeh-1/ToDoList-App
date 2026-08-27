# Source - https://stackoverflow.com/a/51572277
# Posted by martineau, modified by community. See post 'Timeline' for change history
# Retrieved 2026-08-26, License - CC BY-SA 4.0

from tkinter import *

# Button callbacks (which are NOT event handlers)
def display_music():
    music = favoriteMusician.get()
    outputEntry.delete(0, 'end')
    outputEntry.insert(0, f'Your favorite musician is {music}')

def divide():
    answer = str(int(num1Entry.get())/int(num2Entry.get()))
    divideEntry.delete(0, 'end')
    divideEntry.insert(0, answer)


root = Tk()

# Row 0
label1 = Label(root, text='Who is your favorite musician?')
label1.grid(row=0, column=0, sticky=E)

favoriteMusician = Entry(root)
favoriteMusician.grid(row=0, column=1, sticky=W)

# Row 1
b1 = Button(root, text='Output:', command=display_music)
b1.grid(row=1, column=0, sticky=E)
#b1.bind('<Button-1>', display_music)

outputEntry = Entry(root, width=30)
#outputEntry.grid(row=1, column=1, columnspan=2, sticky=W)
outputEntry.grid(row=1, column=1, sticky=W)

# Row 2
mathFrame = Frame(root)
mathFrame.grid(row=2, column=0, columnspan=4)

num1Entry = Entry(mathFrame)
num1Entry.grid(row=2, column=0, sticky=W)

label2 = Label(mathFrame, text='/')
label2.grid(row=2, column=1, sticky=W)

num2Entry = Entry(mathFrame)
num2Entry.grid(row=2, column=2, sticky=W)

b2 = Button(mathFrame, text='=', command=divide)
b2.grid(row=2, column=3, sticky=W)
#b2.bind('<Button-1>', divide)

divideEntry = Entry(mathFrame)
divideEntry.grid(row=2, column=4, sticky=W)


root.mainloop()
