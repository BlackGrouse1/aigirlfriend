import json

path = "session.json"

def get_voice_id():
    with open(path, 'r', encoding='utf-8') as f:
        file_data = json.load(f)

        voice_id = file_data['voice_id']
        file_data['voice_id'] += 1

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file_data, f, ensure_ascii=False, indent=4)

    print(voice_id)
    return voice_id