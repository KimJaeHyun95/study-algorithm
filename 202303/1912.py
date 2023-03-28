N = int(input())

T = list(map(int, input().rstrip().split(' ')))

ans = T[:]

for i in range(1, N):
    ans[i] = max(ans[i], ans[i-1] + T[i])


print(max(ans))