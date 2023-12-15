import os

def modify(path):
    new_lines = []
    with open(path,'r+') as f:
        for line in f:
            new_lines.append(line.replace("python","class"))
        f.seek(0,0)
        for line in new_lines:
            f.write(line)

def func(dir_path):
    for file in os.listdir(dir_path):
        modify(dir_path + f'/{file}')

func('./test')