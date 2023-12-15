num = int(input("Enter a positive Integer: "))
factor = []
copy = num
d = 2
while d < num:
    while num%d == 0:
        factor.append(str(d))
        num //= d
    d += 1

if copy == num:
    factor.append('1')
if num != 1:
    factor.append(str(num))

print("{}={}".format(copy,'*'.join(factor)))
          