N = int(input())

dp = [1] * 10
dp[0] = 0

for i in range(N-1):
    dp = [dp[1], dp[0] + dp[2], dp[1] + dp[3], dp[2] + dp[4], dp[3] + dp[5], dp[4] + dp[6], dp[5] + dp[7], dp[6] + dp[8], dp[7] + dp[9], dp[8]]

print(sum(dp) % 1000000000)
