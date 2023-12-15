year = int(input("Enter a year: "))
if year%100 and year%4 == 0 or year%400 == 0:
    print("Yes")
else:
    print("No")
