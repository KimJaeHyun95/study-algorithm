N = int(input())

T = list(map(int, input().rstrip().split(' ')))

dp = [1] * N

if N >= 2:
    if T[0] < T[1]:
        dp[1] = 2
    else:
        dp[1] = 1

for i in range(2, N):
    dp_max = 1
    for j in range(i):
        if T[j] < T[i]:
            if dp_max <= dp[j] + 1:
                dp_max = dp[j] + 1
    dp[i] = dp_max

print(max(dp))