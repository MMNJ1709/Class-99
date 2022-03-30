import os
import shutil
path="/Users/DELL/OneDrive/Desktop/"
source="/Users/DELL/OneDrive/Desktop/class98_new"
destination="/Users/DELL/OneDrive/Desktop/Class99"
dest=shutil.move(source,destination)
print("after moving file: ")
print(os.listdir(path))