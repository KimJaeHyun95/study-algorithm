N = int(input())

ans = [0 for i in range(N+1)]

ans[1] = 1

if  N >=2:
    ans[2] = 1

for i in range(3, N+1):
    ans[i] = ans[i-2] + ans[i-1]

print(ans[N])