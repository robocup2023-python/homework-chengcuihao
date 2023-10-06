import os

def rename(path):
    files = os.listdir(path)
    os.chdir(path)
    for f in files:
        os.rename(f,f[:-4]+'.png')
    
rename('./img')