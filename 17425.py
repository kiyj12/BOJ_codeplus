# 틀림

dp = [1] * 1000001
sum = [0] * 1000001

# 미리 다 리스트로 만들어두기
for i in range(2, 1000001):  # 전체 돌기
    j = 1
    while i*j <= 1000000:  # 약수인 곳에 다 더하기
        dp[j] += i
        j += 1

for i in range(1, 1000001):
    sum[i] = sum[i-1] + dp[i]

cnt = int(input())
# 입력받자마자 찾아서 출력하기
for i in range(cnt):
    n = int(input())
    print(sum[n])