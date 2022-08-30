# 소수이면 True인 전체 리스트 만들어두기.
sarr = [True for _ in range(1000001)]
for i in range(2, 1001):
    if sarr[i]:
        for j in range(i * 2, 1000001, i):
            sarr[j] = False

while True:
    n = int(input())
    if n == 0:
        break

    done = 0
    for i in range(3, len(sarr)):
        if sarr[i] and sarr[n-i]:
            print(f"{n} = {i} + {n-i}")
            done += 1
            break
    if done == 0:
        print("Goldbach's conjecture is wrong.")