for i in range(7):
    num = 2*i+1 if i < 4 else 13-2*i
    string = '*'*num
    print(string.center(7))
    