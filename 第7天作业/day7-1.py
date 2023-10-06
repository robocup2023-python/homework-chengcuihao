def func(path):
    lst = []
    with open(path,'r') as f:
        line = f.readline()
        while line:
            lst.append(int(line.split(',')[1]))
            line = f.readline()
    lst.sort()
    mean = sum(lst)/len(lst)
    return lst[-1], lst[0], mean, (lst[4]+lst[5])/2





