import numpy as np

lst = sorted(list(np.random.randint(-10000,10000,10)))
num = float(input("Enter a number: "))
for i in range(len(lst)-1,-1,-1):
    if num > lst[i]:
        lst.insert(i+1, num)
        break
if num <= lst[0]:
    lst.insert(0,num)

for i in lst:
    print(i,end=' ')