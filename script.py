#import zipfile

#with zipfile.ZipFile('deep_sort_pytorch.zip', 'r') as zip_ref:
#    zip_ref.extractall()

import torch
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "0"

print("CUDA available:", torch.cuda.is_available())
print("CUDA version:", torch.version.cuda)
print("Number of CUDA devices:", torch.cuda.device_count())
if torch.cuda.is_available():
    print("Current CUDA device:", torch.cuda.current_device())
    print("Device name:", torch.cuda.get_device_name(torch.cuda.current_device()))