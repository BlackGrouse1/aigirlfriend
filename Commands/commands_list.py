from .commands import *

def analyze_message(message: str):
    if message.lower() == "open youtube":
        open_youtube()
        return "command"
    elif message.lower() == "open github":
        open_github()
        return "command"