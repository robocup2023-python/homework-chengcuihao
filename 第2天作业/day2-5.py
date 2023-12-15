for i in range(101, 201):
    d = 2
    while d*d <= i:
        if i%d == 0:
            break
        d += 1
    if d*d > i:
        print(i)
