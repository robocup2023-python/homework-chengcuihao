#  11月1日的题目是哪个呀，因为不太清楚所以直接用第七天最后一个作业来代替了
import os

def modify(path: str) -> None: 
    new_lines:list[str]  = []
    with open(path,'r+') as f:
        for line in f:
            new_lines.append(line.replace("python","class"))
        f.seek(0,0)
        for line in new_lines:
            f.write(line)

def func(dir_path: str) -> None:
    for file in os.listdir(dir_path):
        modify(dir_path + f'/{file}')

