import random, shutil

def create(n,path):
    with open('path','w') as f:
        for i in range(n):
            word_num = random.randint(0,100)
            for j in range(word_num):
                f.write(chr(random.randint(32,127)))
            f.write('\n')

def copy(path, dest):
    shutil.copy(path,dest)


