a = int(input("Enter an Integer: "))
b = int(input("Number of addition: "))
d = 0
lst = [a]
while a:
    d += 1
    a //= 10
for i in range(b-1):
    lst.append(lst[-1]*10**d+lst[0])
print(sum(lst))