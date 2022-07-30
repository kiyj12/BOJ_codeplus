while True:
    try:
        n = int(input())
    except:
        break

    i = 0 # 반복횟수 즉 지수
    k = 0 # 결과값 1로만만들어진.
    while True:
        k = k + 10 ** i
        r = k % n
        if r == 0:
            print(i + 1)
            break
        i += 1

