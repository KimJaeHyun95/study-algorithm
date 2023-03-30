N = int(input())

T = [list(map(int, input().rstrip().split(' '))) for i in range(N)]

ans = [[0 for j in range(i+1)] for i in range(N)]

ans[0][0] = T[0][0]

for i in range(1, N):
    for j in range(i+1):
        if j == 0:
            ans[i][j] = ans[i-1][0] + T[i][0]
        elif j == i:
            ans[i][j] = ans[i-1][i-1] + T[i][i]
        else:
            ans[i][j] = T[i][j] + max(ans[i-1][j-1], ans[i-1][j])

print(max(ans[N-1]))