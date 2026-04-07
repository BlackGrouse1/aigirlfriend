import json
import os

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

def clear_voice_id():
    with open(path, 'r', encoding='utf-8') as f:
        file_data = json.load(f)
        voice_id = file_data['voice_id']
        file_data['voice_id'] = 0

    for i in range(voice_id):
        file_path = f"Audios/generated/girly_voice_{i}.wav"
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except PermissionError:
            print(f"error deleting {file_path}")
        except Exception as e:
            print(e)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(file_data, f, ensure_ascii=False, indent=4)

    print("Success")
    return True