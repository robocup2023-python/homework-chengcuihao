num = int(input("Enter a positive Integer: "))
d = 0
while num:
    print(num%10, end='')
    d += 1
    num //= 10
print()
print("digit: ", d)