import kagglehub
import shutil
import os

default_path = kagglehub.dataset_download("parulpandey/palmer-archipelago-antarctica-penguin-data")
print(default_path)
target_dir = '/Users/bw/GITS/ITMO/Penguins_Data_Science/data'
os.makedirs(target_dir, exist_ok=True)
for item in os.listdir(default_path):
    src_item = os.path.join(default_path, item)
    dst_item = os.path.join(target_dir, item)
    shutil.move(src_item, dst_item)
print("Moved to:", target_dir)