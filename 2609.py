a, b = input().split()
a = int(a)
b = int(b)

if a == b:
    print(a)
    print(b)
else:
    tmp = min(a, b)
    b = max(a, b)
    a = tmp
    l = []
    for i in range(1, a + 1):
        if a % i == 0 and b % i == 0:
            l.append(i)
    lcm = max(l)
    print(lcm)
    print(lcm * (a // lcm) * (b // lcm))
