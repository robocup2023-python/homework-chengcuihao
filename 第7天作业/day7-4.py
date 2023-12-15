def func(path1, path2):
    with open(path1, 'r') as f1:
        with open(path2, 'r') as f2:
            s1,s2 = f1.readline(),f2.readline()
            line = 0
            while s1 or s2:
                line += 1
                if s1 != s2:
                    print(line)
                s1,s2 = f1.readline(),f2.readline()


        