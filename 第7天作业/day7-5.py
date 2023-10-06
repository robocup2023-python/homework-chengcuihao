import os, random


def create(n,path):
    with open(path,'w') as f:
        for i in range(n):
            word_num = random.randint(0,100)
            for j in range(word_num):
                f.write(chr(random.randint(32,127)))
            f.write('\n')


def add(path):
    with open(path, 'r+') as f:
        f.seek(0,0)
        lines = []
        line = f.readline()
        while line:
            lines.append(line)
            line = f.readline()
        f.seek(0,0)
        for i in range(len(lines)):
            f.write(lines[i][:-1])
            f.write("-python\n")
        f.flush()

def create_add():
    num_flies = int(input("Enter the number of files: "))
    lines = int(input("Random lines of every files: "))
    path = './test'
    os.mkdir(path)
    for i in range(num_flies):
        create(lines, path+f'/test{i+1}.txt')
    for file in os.listdir(path):
        add(path+'/' + file)

create_add()