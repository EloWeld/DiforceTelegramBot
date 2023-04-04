import os

import pyperclip

def find_python_files(path):
    python_files = []
    
    for entry in os.scandir(path):
        if entry.is_file() and entry.name.endswith('.py') and entry.name not in ['ai.py']:
            python_files.append(entry.path)
        elif entry.is_dir() and entry.name not in ['venv', '__pychache__', '.vscode', '.git']:
            python_files.extend(find_python_files(entry.path))
    
    return python_files


if __name__ == '__main__':
    folder_path = '.'
    output_file = 'output.txt'

    python_files = find_python_files(folder_path)
    output_data = ""
    isfirst = False
    for file in python_files:
        if not isfirst:
            output_data += "Вот мой код: \"\"\""
        else:
            output_data += "\"\"\"\nЕщё у меня есть файл {file}, вот его содержимое:\n\"\"\""
        isfirst = True
        with open(file, 'r') as infile:
            content = infile.read()
            output_data += content
    output_data += "\"\"\"\n"
            
    pyperclip.copy(output_data)
    with open(output_file, 'w') as outfile:
        outfile.write(output_data)

      