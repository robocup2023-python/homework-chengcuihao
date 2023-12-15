import random
n = int(input("n: "))
m = int(input("m: "))
if m > n:
    print("m must be less than n")
else:
    lst = []
    for i in range(n):
        lst.append(random.randint(0,100))
    print("oringinal list: ", lst)
    for i in range(m):
        lst.insert(0,lst.pop(-1))
    print("after movement: ", lst)

