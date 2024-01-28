from tkinter import *
from PIL import ImageTk, Image
import os
import onetimepad
from tkinter import messagebox


def encryptMessage():
    title = entry.get().strip()
    masterKey = entry1.get().strip()

    if not title:
        messagebox.showerror("Error", "Please enter a title.")
        return

    if not masterKey:
        messagebox.showerror("Error", "Please enter a valid masterkey")
        return

    else:
        messagebox.showinfo("Masterkey generated")

    pt = text.get("1.0", "end-1c")
    ct = onetimepad.encrypt(pt, masterKey)

    file_path = f"{title}.txt"

    with open(file_path, "w") as file:
        file.write(ct)


def decryptMessage():
    title = entry.get().strip()
    masterKey = entry1.get().strip()

    if not title:
        messagebox.showerror("Error", "Please enter a title.")
        return

    if not masterKey:
        messagebox.showerror("Error", "Please enter a valid masterkey")
        return

    file_path = f"{title}.txt"

    if not os.path.exists(file_path):
        messagebox.showerror("Error", f"The file '{file_path}' does not exist.")
        return

    with open(file_path, "r") as file:
        ct1 = file.read()

    pt1 = onetimepad.decrypt(ct1, masterKey)
    text.delete("1.0", END)
    text.insert(END, pt1)



page = Tk()

page.minsize(width=300, height=300)
page.config(padx=30, pady=30)

canvas = Canvas(page, width=250, height=250)
canvas.pack()

image_path = r"C:\Users\efeba\OneDrive\Masaüstü\pic\secret.png"

if os.path.exists(image_path):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((200, 200), Image.LANCZOS)
    img = ImageTk.PhotoImage(resized_image)
    canvas.create_image(20, 20, anchor=NW, image=img)

else:
    print(f"Error: The file '{image_path}' does not exist.")


label1 = Label(text="Title")
label1.pack()

entry = Entry(width=30)
entry.pack()

label2 = Label(text="Enter your secret")
label2.pack()

text = Text(width=30, height=20)
text.pack()

label3 = Label(text="ENTER MASTER KEY" , font="Verdana 14")
label3.pack(expand=True)

entry1 = Entry(width=30)
entry1.pack()

encryption_button = Button(text="Save & Encrypt", command=encryptMessage)
encryption_button.config(pady=5)
encryption_button.pack(pady=5)

decrypt_button = Button(text="Decrypt", command=decryptMessage)
decrypt_button.config(pady=5)
decrypt_button.pack(pady=5)

page.mainloop()
