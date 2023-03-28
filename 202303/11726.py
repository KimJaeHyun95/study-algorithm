N = int(input())

ans = [0] * (N+1)

ans[1] = 1

if N >= 2:
    ans[2] = 2

n = 3
while n < N+1:
    ans[n] = ans[n-1] + ans[n-2]
    n+=1

print(ans[N]%10007)