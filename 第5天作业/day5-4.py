import os


def create_dir():
    os.mkdir('./img')

    for i in range(1,100):
        with open('./img/%d.png'%(i),'wb'):
            pass
