N = int(input())

numl = map(int, input().split())

scnt = 0

for num in numl:
    nos = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                nos += 1
        if nos == 0:
            scnt += 1


print(scnt)