string = input("Enter a positive Integer: ")
flag = True
for i in range(len(string)):
    if string[i] != string[len(string)-1-i]:
        flag = False
        break
print('Yes' if flag else 'No')