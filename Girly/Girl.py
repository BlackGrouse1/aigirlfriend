from pathlib import Path

Path(__file__).parent.parent

from Speech import text2speech
from Mind import ai_chatt

class Girl:
    def __init__(self):
        pass

    def dialog(self, message: str):
        res = ai_chatt(message)
        text2speech(res)