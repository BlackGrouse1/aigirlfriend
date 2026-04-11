from download_model import downloading_model
from Girly import Girl
from history import clear_history

import os

girly = Girl()

def main():
    if not os.path.exists("models"):
        downloading_model()
    
    girly.mainloop()

if __name__ == "__main__":
    main()
    clear_history()