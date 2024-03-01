import textwrap
from tkinter.filedialog import askopenfilename
import re
import os

def get_name(path):
    filename = os.path.basename(path)
    return os.path.splitext(filename)[0]

def convert_md_to_txt(md_file_path, txt_file_path):
    with open(md_file_path, 'r') as md_file:
        lines = md_file.readlines()

    wrapper = textwrap.TextWrapper(width=40)
    wrapped_lines = [wrapper.fill(line) for line in lines]

    with open(txt_file_path, 'w') as txt_file:
        txt_file.write('\n'.join(wrapped_lines))


def requestFile():
  filepath = askopenfilename()
  if type(filepath) is str:
    return filepath
  else:
    return "."

# Usage

filepath = requestFile()
print(get_name(filepath))
new_file = f"Converted\{get_name(filepath)}.txt"
convert_md_to_txt(filepath, new_file)