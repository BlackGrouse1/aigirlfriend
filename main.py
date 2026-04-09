from download_model import downloading_model
from Girly import Girl
from history import clear_history

import os

girly = Girl()

def main():
    if not os.path.exists("models"):
        downloading_model()
    try:
        while True:
            mess = input("Your message >> ")
            if mess == "!STOP":
                clear_history()
                print("Break...")
                break

            girly.dialog(mess)
            # res = ai_chatt(mess)
            # text2speech(res)
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()