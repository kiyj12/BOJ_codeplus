# 규칙 존재! 정답 리스트 먼저 만들어 두기.
dp = [0, 1, 2, 4]

for i in range(4, 12):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])