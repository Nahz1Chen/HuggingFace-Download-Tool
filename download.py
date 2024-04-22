# from huggingface_hub import snapshot_download

# snapshot_download(repo_id="runwayml/stable-diffusion-v1-5",local_dir='D:/stable-diffusion-v1-5',resume_download=True,proxies='127.0.0.1:7890')

import os
from huggingface_hub import snapshot_download
# 如果需要代理的话，去掉此部分注释加入端口
os.environ["https_proxy"] = "127.0.0.1:7890" # 代理设置
# os.environ["http_proxy"] = "http://xxxxxxx:xxxx" # 代理设置
repo_id = "yangtao9009/DIV2K" # 模型在huggingface上的名称
cache_dir = "./cache/"
local_dir = "D:/DIV2K"
# 指定要创建的目录路径

local_dir_use_symlinks = False # 本地模型使用文件保存，而非blob形式保存
#
# token = "XXXXXXXXXX" # 在hugging face上生成的 access token

# 检查目录是否存在
if not os.path.exists(cache_dir):
 # 创建目录
    os.makedirs(cache_dir)
#
if not os.path.exists(local_dir):
 # 创建目录
    os.makedirs(local_dir)
#
snapshot_download(
 repo_id=repo_id,
 repo_type='dataset',#Accepted repo types are: [None, 'model', 'dataset', 'space']
 cache_dir=cache_dir,
 local_dir=local_dir,
 local_dir_use_symlinks=local_dir_use_symlinks,
 force_download=True,
 resume_download=True
)
print("======Download successful=====")
