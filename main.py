from Speech import *
from Mind import *
from Visual import *

def main():
    try:
        while True:
            # clear_voice_id()
            mess = input("Your message >> ")
            if mess == "!STOP":
                print("Break...")
                break

            res = ai_chatt(mess)
            text2speech(res)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()