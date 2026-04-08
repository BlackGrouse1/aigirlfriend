from Speech import *
from Mind import *
from Visual import *

def main():
    if not os.path.exists("models"):
        downloading_model()
    try:
        while True:
            mess = input("Your message >> ")
            if mess == "!STOP":
                reclear_voice_id()
                print("Break...")
                break
            # mess = display()


            res = ai_chatt(mess)
            text2speech(res)
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    main()