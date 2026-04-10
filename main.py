from download_model import downloading_model
from Girly import Girl
from history import clear_history

import os

import tkinter as tk
from tkinter import Entry, Label

from PIL import Image, ImageTk

girly = Girl()
photo0 = "Pictures/ex1.jpeg"

def main():
    if not os.path.exists("models"):
        downloading_model()
    try:
        root = tk.Tk()
        root.title("Display:)")
        root.geometry("900x500")

        image = Image.open(photo0)
        image = image.resize((700, 400))
        photo = ImageTk.PhotoImage(image)

        image_label = Label(root, image=photo)
        image_label.pack(pady=10)

        entry_label = Label(root, text="TYPE...")
        entry_label.pack()
         
        entry = Entry(root, width=30)
        entry.pack(pady=5)

        def get_message():
            message = entry.get()
            result_label.config(text=f"Text: {message}")
            if message == "!STOP":
                root.destroy()
                clear_history()
            else:
                girly.dialog(message)
            
        submit_button = tk.Button(root, text="Send", command=get_message)
        submit_button.pack(pady=10)

        result_label = Label(root, text="")
        result_label.pack()

        root.mainloop()
        return True
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()