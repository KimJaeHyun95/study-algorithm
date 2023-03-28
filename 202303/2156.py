N = int(input())

T = []

[T.append(int(input())) for i in range(N)]

ans = [0] * (N+1)

ans[1] = T[0]

if N >=2:
    ans[2] = T[0] + T[1]


for i in range(3, N+1):
    ans[i] = max(ans[i-1], ans[i-2] + T[i-1], ans[i-3] + T[i-2] + T[i-1])

print(ans[N])