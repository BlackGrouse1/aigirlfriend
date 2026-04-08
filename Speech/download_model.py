from huggingface_hub import snapshot_download
import os

model_id = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"
local_dir = "./models/Qwen3-TTS"

def downloading_model():
    print("Downloading complete model...")
    try:
        snapshot_download(
            repo_id=model_id,
            local_dir=local_dir,
            local_dir_use_symlinks=False,
            resume_download=True,
            ignore_patterns=["*.h5", "*.ot", "*.msgpack"],
        )
        print(f"Model downloaded to: {local_dir}")
        
        print("\nDownloaded files:")
        for root, dirs, files in os.walk(local_dir):
            level = root.replace(local_dir, '').count(os.sep)
            indent = ' ' * 2 * level
            print(f"{indent}{os.path.basename(root)}/")
            subindent = ' ' * 2 * (level + 1)
            for file in files[:10]:
                print(f"{subindent}{file}")
                
    except Exception as e:
        print(f"Error downloading: {e}")