from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("denomination counter")
root.configure(bg="lightblue")
root.geometry("650x400")
upload = Image.open("app_img.jpg")
upload = upload.resize((300, 300))
image = ImageTk.PhotoImage(upload)

label = Label(root,image=image,bg="Lightblue")
label.place(x=180,y=20)

label1 = label(
    root,
    text="hey user! welcome to denomination counter application"
    bg="lightblue"
)

label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
        "alert",
        "do you want to calulate the denomination count??"

    )
    if MsgBox=="OK
    "