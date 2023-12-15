dic = dict(zip([i for i in range(1,13)],[31,28,31,30,31,30,31,31,30,31,30,31]))
y,m,d = map(int, input("Enter year/month/day: ").split("/"))
ans = d
for i in range(1,m):
    ans += dic[i]
if m > 2:
    if y%400 == 0 or y%100 and y%4 == 0:
        ans += 1
print(ans)