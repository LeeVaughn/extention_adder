from sys import argv
import os


path = "./files_to_rename"
script, filetype = argv

# add audio file type to file name
for filename in os.listdir(path):
    os.rename(os.path.join(path,filename),os.path.join(path, filename.replace('.txt', f'{filetype}.txt')))

# run with `py rename_files.py <filetype>`
