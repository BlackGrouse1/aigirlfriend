from Speech import *
from Mind import *
from Visual import *

def main():
    try:
        while True:
            mess = input("Your message >> ")
            if mess == "!STOP":
                clear_voice_id()
                print("Break...")
                break

            res = ai_chatt(mess)
            text2speech(res)
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()