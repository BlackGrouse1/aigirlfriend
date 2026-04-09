import json
from pathlib import Path

Path(__file__).parent.parent

path = "session.json"

def get_last_message(message: str):
    with open(path, 'r', encoding='utf-8') as f:
        file_data = json.load(f)

        last_mess = file_data['last_message']
        last_ans = file_data['last_answer']
        
        if last_mess != "":
            new_message = f"my last message: {last_mess}; ur last answer: {last_ans};\n\n{message}"
        elif last_mess == "":
            new_message = message

        file_data['last_message'] = message

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file_data, f, ensure_ascii=False, indent=4)

    return new_message

def set_new_answer(answer: str):
    with open(path, 'r', encoding='utf-8') as f:
        file_data = json.load(f)

        file_data['last_answer'] = answer

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file_data, f, ensure_ascii=False, indent=4)

    return answer