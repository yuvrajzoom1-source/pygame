from tkinter import *
from tkinter import messagebox

tasks = ["Homework", "Play", "Dinner", "Sleep"]

def show_char(event):
    text = entry.get()
    if text:
        label["text"] = text[-1]
    else:
        messagebox.showwarning("Oops!", "Type something first!")

def next_task():
    next_task.index += 1
    if next_task.index <= len(tasks):
        label["text"] = tasks[next_task.index - 1]
    else:
        label["text"] = "Done!"

next_task.index = 0

root = Tk()

entry = Entry(root)
entry.pack()
entry.bind("<KeyRelease>", show_char)

button = Button(root, text="Next Task", command=next_task)
button.pack()

label = Label(root, text="Start typing...")
label.pack()

root.mainloop()