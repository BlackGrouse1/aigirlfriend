from pathlib import Path
import customtkinter as ctk
import playsound as ps

Path(__file__).parent.parent

from Speech import text2speech
from Mind import ai_chatt
from history import clear_history

class Girl(ctk.CTk):
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
                
        self.entry = ctk.CTkEntry(self, width=500, height=45, 
                                  placeholder_text="TYPE YOUR MESSAGE...",
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


    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    def dialog(self, message: str):
        res = ai_chatt(message)
        text2speech(res)

    def draw_glowing_circle(self):
        colors = ["#00f0ff", "#00d0ff", "#00a0ff"]
        for i, color in enumerate(colors):
            width = 18 - i*5
            self.canvas.create_oval(40 + i*15, 40 + i*15, 
                                    340 - i*15, 340 - i*15,
                                    outline=color, width=width)
        

    def send_message(self):
        message = self.entry.get().strip()
        if not message:
            return
            
        # self.result_text.insert("end", f"> {message}\n")
        self.result_text.see("end")
        self.entry.delete(0, "end")
        
        if message.upper() == "!STOP":
            self.destroy()
            clear_history()
        else:
            try:
                response = self.dialog(message)
                # self.result_text.insert("end", f"Girly: {response}\n\n")
            except Exception as e:
                self.result_text.insert("end", f"Error: {e}\n")()