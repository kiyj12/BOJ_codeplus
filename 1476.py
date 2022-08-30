E, S, M = input().split()
E = int(E)
S = int(S)
M = int(M)

a = 0
b = 0
c = 0
err = 0
while True:
    while (b * 28 + S) >= (c * 19 + M):
        while (c * 19 + M) >= (a * 15 + E):
            if (b * 28 + S) == (c * 19 + M) == (a * 15 + E):
                print(f"{a * 15 + E}")
                err += 1
                break
            else:
                a += 1
        if err > 0:
            break
        c += 1
    if err > 0:
        break
    b += 1

