m, n = input().split()
m = int(m)
n = int(n)

slist = []
for i in range(m, n+1):
    err = 0
    if i > 1:
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                err += 1
                break
        if err == 0:
            slist.append(i)


for s in slist:
    print(s)
