def caculate(*args):
    index = []
    mean = sum(args) / len(args)
    for i in range(len(args)):
        if args[i] > mean:
            index.append(i)
    return (mean, index)

