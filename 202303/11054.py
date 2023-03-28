N = int(input())

T = list(map(int, input().rstrip().split(' ')))

# 증가하는 수열
dp1 = [1] * N

# 뒤에서 부터 증가 수열
dp2 = [1] * N


if N >= 2:
    if T[0] < T[1]:
        dp1[1] = 2
    else:
        dp1[1] = 1

    if T[N-1] < T[N-2]:
        dp2[N-2] = 2
    else:
        dp2[N-2] = 1

for i in range(2, N):
    dp_max = 1
    for j in range(i):
        if T[j] < T[i]:
            if dp_max <= dp1[j] + 1:
                dp_max = dp1[j] + 1
    dp1[i] = dp_max

    dp2_max = 1
    for j in range(i):
        if T[N-j-1] < T[N-i-1]:
            if dp2_max <= dp2[N-j-1] + 1:
                dp2_max = dp2[N-j-1] + 1
    dp2[N-i-1] = dp2_max

dp = [1] * N
for i in range(N):
    dp[i] = dp1[i] + dp2[i] -1

print(max(dp))