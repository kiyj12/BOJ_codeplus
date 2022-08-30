arr = [0 for _ in range(9)]
for i in range(9):
    n = int(input())
    arr[i] = n


for i in range(8):
    for j in range(i+1,9):
        t = sum(arr) - arr[i] - arr[j]
        if t == 100:
            arr[i] = 0
            arr[j] = 0
            arr.sort()
            for k in range(2, 9):
                print(arr[k])
