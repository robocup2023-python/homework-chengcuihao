h = 100
tot = h
for i in range(9):
    h /= 2
    tot += h*2
print("total distance:", tot)
print("The 10th rebound height is", h/2)
   