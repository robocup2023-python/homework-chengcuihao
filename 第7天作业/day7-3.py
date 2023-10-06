def func(path):
    with open(path, 'r+') as f:
        f.seek(0,0)
        ori = f.read()
        f.seek(0,0)
        f.write("python")
        f.write(ori)
        f.write("python")
        f.flush()


