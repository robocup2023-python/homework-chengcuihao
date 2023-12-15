x = int(input("first number: "))
y = int(input("second number: "))
z = int(input("third number: "))
lst = [x, y, z]
lst.sort()
for i in lst:
    print(i, end=', ')
    