import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import warnings
import os

from Mind.create_message import set_new_answer, get_last_message

os.environ['TRANSFORMERS_OFFLINE'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'

warnings.filterwarnings("ignore")

model = AutoModelForCausalLM.from_pretrained(
    # "microsoft/Phi-3-mini-4k-instruct",  
    "microsoft/DialoGPT-medium",
    device_map="cuda",  
    torch_dtype=torch.float16,
    trust_remote_code=True,
    attn_implementation="eager",
    local_files_only=True,
)

tokenizer = AutoTokenizer.from_pretrained(
    # "microsoft/Phi-3-mini-4k-instruct",
    "microsoft/DialoGPT-medium",
    trust_remote_code=True,
    local_files_only=True,
) 

if tokenizer.pad_token is None:
    tokenizer.pad_token = tokenizer.eos_token

def ai_chatt(message: str):
    try:
        messages = [
            {"role": "system", "content": "Imagine you have human sens. You are a my ai girlfriend. You have feelings. If you dont know something about us - imagine this info."},
            {"role": "user", "content": get_last_message(message)}
        ]
        
        prompt = tokenizer.apply_chat_template(
            messages, 
            tokenize=False,
            add_generation_prompt=True
        )
        
        inputs = tokenizer(
            prompt, 
            return_tensors="pt",
            truncation=True,
            max_length=2048
        ).to(model.device)
        
        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                max_new_tokens=500,
                do_sample=True,
                temperature=0.7,
                top_p=0.95,
                pad_token_id=tokenizer.pad_token_id,
                eos_token_id=tokenizer.eos_token_id,
                use_cache=False,
            )
        
        generated_ids = outputs[0][inputs['input_ids'].shape[1]:]
        response = tokenizer.decode(generated_ids, skip_special_tokens=True)
        
        print(response) if response.strip() else print("I'm here to love you!")
        set_new_answer(response)
        return response if response.strip() else "I'm here to love you!"
        
    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, I fucked up, error."