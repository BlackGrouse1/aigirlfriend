# from download_model import downloading_model
# from Girly import Girl
# from history import clear_history

# import os

# import tkinter as tk
# from tkinter import Entry, Label

# from PIL import Image, ImageTk

# girly = Girl()
# photo0 = "Pictures/ex1.jpeg"

# def main():
#     if not os.path.exists("models"):
#         downloading_model()
#     try:
#         root = tk.Tk()
#         root.title("Display:)")
#         root.geometry("900x500")

#         image = Image.open(photo0)
#         image = image.resize((700, 400))
#         photo = ImageTk.PhotoImage(image)

#         image_label = Label(root, image=photo)
#         image_label.pack(pady=10)

#         entry_label = Label(root, text="TYPE...")
#         entry_label.pack()
         
#         entry = Entry(root, width=30)
#         entry.pack(pady=5)

#         def get_message():
#             message = entry.get()
#             result_label.config(text=f"Text: {message}")
#             if message == "!STOP":
#                 root.destroy()
#                 clear_history()
#             else:
#                 girly.dialog(message)
            
#         submit_button = tk.Button(root, text="Send", command=get_message)
#         submit_button.pack(pady=10)

#         result_label = Label(root, text="")
#         result_label.pack()

#         root.mainloop()
#         return True
#     except Exception as e:
#         print(e)


# if __name__ == "__main__":
#     main()











import customtkinter as ctk
from PIL import Image, ImageTk
import os

from download_model import downloading_model
from Girly import Girl
from history import clear_history

girly = Girl()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class GirlyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        self.title("Girly v0.0.0")
        self.geometry("900x620")
        self.resizable(False, False)
        
        self.configure(fg_color="#0a0e17")
        
        self.canvas = ctk.CTkCanvas(self, width=380, height=380, 
                                    bg="#0a0e17", highlightthickness=0)
        self.canvas.place(x=260, y=120)
        
        self.draw_glowing_circle()
        
        title = ctk.CTkLabel(self, text="Girly", 
                             font=ctk.CTkFont(family="Arial", size=32, weight="bold"),
                             text_color="#00f0ff")
        title.place(x=50, y=30)
        
        version = ctk.CTkLabel(self, text="v0.0.0", 
                               font=ctk.CTkFont(size=14),
                               text_color="#00f0ff")
        version.place(x=50, y=70)
        
        self.create_status_bar()
        
        self.entry = ctk.CTkEntry(self, width=500, height=45, 
                                  placeholder_text="TYPE YOUR COMMAND...",
                                  font=ctk.CTkFont(size=16))
        self.entry.place(x=200, y=520)
        
        send_btn = ctk.CTkButton(self, text="SEND", width=120, height=45,
                                 font=ctk.CTkFont(size=16, weight="bold"),
                                 fg_color="#00f0ff", text_color="black",
                                 hover_color="#00c0d0",
                                 command=self.send_message)
        send_btn.place(x=720, y=520)
        
        self.result_text = ctk.CTkTextbox(self, width=800, height=80,
                                          fg_color="#11161f", text_color="#00ffcc")
        self.result_text.place(x=50, y=580)
        
        if os.path.exists("Pictures/ex1.jpeg"):
            img = Image.open("Pictures/ex1.jpeg").resize((120, 120))
            self.photo = ImageTk.PhotoImage(img)
            img_label = ctk.CTkLabel(self, image=self.photo, text="")
            img_label.place(x=50, y=120)

    def draw_glowing_circle(self):
        colors = ["#00f0ff", "#00d0ff", "#00a0ff"]
        for i, color in enumerate(colors):
            width = 18 - i*5
            self.canvas.create_oval(40 + i*15, 40 + i*15, 
                                    340 - i*15, 340 - i*15,
                                    outline=color, width=width)
        
        self.canvas.create_oval(140, 140, 240, 240, fill="#ffffff", outline="#00f0ff", width=8)

    def create_status_bar(self):
        mic_frame = ctk.CTkFrame(self, fg_color="transparent")
        mic_frame.place(x=80, y=460)
        ctk.CTkLabel(mic_frame, text="●", text_color="#ff0000", font=ctk.CTkFont(size=20)).pack(side="left")
        ctk.CTkLabel(mic_frame, text="Microphone\ninactive", text_color="#ffaaaa").pack(side="left", padx=8)
        
        nn_frame = ctk.CTkFrame(self, fg_color="transparent")
        nn_frame.place(x=380, y=460)
        ctk.CTkLabel(nn_frame, text="●", text_color="#ffcc00", font=ctk.CTkFont(size=20)).pack(side="left")
        ctk.CTkLabel(nn_frame, text="AI\nmicrosoft/DialoGPT-medium + Qwen3-TTS", text_color="#ffdd88").pack(side="left", padx=8)
        
        # res_frame = ctk.CTkFrame(self, fg_color="transparent")
        # res_frame.place(x=680, y=460)
        # ctk.CTkLabel(res_frame, text="●", text_color="#4488ff", font=ctk.CTkFont(size=20)).pack(side="left")
        # ctk.CTkLabel(res_frame, text="Resurses\nAll systems OK", text_color="#88aaff").pack(side="left", padx=8)

    def send_message(self):
        message = self.entry.get().strip()
        if not message:
            return
            
        self.result_text.insert("end", f"> {message}\n")
        self.result_text.see("end")
        self.entry.delete(0, "end")
        
        if message.upper() == "!STOP":
            self.destroy()
            clear_history()
        else:
            try:
                response = girly.dialog(message)  # или girly.get_response(message)
                self.result_text.insert("end", f"Girly: {response}\n\n")
            except Exception as e:
                self.result_text.insert("end", f"Error: {e}\n")


if __name__ == "__main__":
    if not os.path.exists("models"):
        downloading_model()
    
    app = GirlyApp()
    app.mainloop()