import re
def read_matrix(row, col):
    res = []
    while(len(res) < row*col):
        tem = input()
        for i in re.findall(r"\d+",tem):
            res.append(i)
    return res

X = read_matrix(3,3)
Y = read_matrix(3,3)
Z = [str(int(X[i])+int(Y[i])) for i in range(9)]
for i in range(3):
    print('['+','.join(Z[3*i:3*i+3])+']')
    
        
        


