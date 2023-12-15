num_list = [1, 2, 3, 4]
res = []
for i in num_list:
    for j in num_list:
        for k in num_list:
            if  i != j and j != k and i != k:
                res.append(i+10*j+100*k)
print("numbers: ", len(res))
print(res)

