import torch
import soundfile as sf
from qwen_tts import Qwen3TTSModel

from playsound import playsound
import os

from Speech.get_voice_id import get_voice_id

os.environ['TRANSFORMERS_OFFLINE'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'

model_path = r"./models/Qwen3-TTS"

model = Qwen3TTSModel.from_pretrained(
    model_path,
    device_map="cuda:0",
    dtype=torch.bfloat16,
    local_files_only=True,
    )

ref_audio = "megan.mp3"
ref_text = "most of you probably know me from naked pictures on the internet. There are a lot of those out there, which is weird because I don’t remember ever posing nude. But, I mean, I must have because how else could they exist, right?"

def text2speech(message: str):
    result = model.generate_voice_clone(
        text=message,
        language="English",
        ref_audio=ref_audio,
        ref_text=ref_text,
        )

    wavs, sr = result[0], result[1]

    output_file_for_audios = "Audios/generated"
    if not os.path.exists(output_file_for_audios):
        os.mkdir("Audios/generated")

    output_file = f"Audios/generated/girly_voice_{get_voice_id()}.wav" #Audios/generated/
    # output_file = "Audios/generated/girly_voice_.wav" #Audios/generated/

    sf.write(output_file, wavs[0], sr)
    playsound(output_file)