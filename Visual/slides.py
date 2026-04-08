# import cv2

# photo0 = "Pictures/ex1.jpeg"

# def show_window():
#     image = cv2.imread(photo0)
#     cv2.imshow("my girly", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

import tkinter as tk
from tkinter import Entry, Label

from PIL import Image, ImageTk


from Mind import ai_chatt
from Speech import text2speech

photo0 = "Pictures/ex1.jpeg"

def display():
    try:
        root = tk.Tk()
        root.title("Display:)")
        root.geometry("800x400")

        # image = Image.open(photo0)
        # # image.resize([200, 300])

        # photo = ImageTk.PhotoImage(image)

        # image_label = Label(root, image=photo)
        # image_label.pack(pady=10)

        entry_label = Label(root, text="TYPE...")
        entry_label.pack()

        entry = Entry(root, width=30)
        entry.pack(pady=5)

        # message = ""
        def get_message():
            message = entry.get()
            result_label.config(text=f"Text: {message}")
            print(f"Message: {message}")

            res = ai_chatt(message)
            text2speech(res)
        
        submit_button = tk.Button(root, text="Send", command=get_message)
        submit_button.pack(pady=10)
        
        result_label = Label(root, text="")
        result_label.pack()

        root.mainloop()
        return True
    except Exception as e:
        print(e)

display()