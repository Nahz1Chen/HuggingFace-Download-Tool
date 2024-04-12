from huggingface_hub import snapshot_download

snapshot_download(repo_id="runwayml/stable-diffusion-v1-5",local_dir='D:/stable-diffusion-v1-5',resume_download=True)