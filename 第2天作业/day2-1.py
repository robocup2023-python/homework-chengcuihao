string = input("Enter a string: ")
alpha = space = digit = other = 0
for s in string:
    if s.isalpha(): 
        alpha += 1
    elif s.isdigit():
        digit += 1
    elif s == ' ':
        space += 1
    else:
        other += 1

print(alpha, space, digit, other)