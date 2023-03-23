N, M = list(map(int, input().rstrip().split(' ')))

T = [list(map(int, input().rstrip().split(' '))) for i in range(M)]

V = [0 for i in range(N+1)]

def sol(n):
    if V[T[n][0]] == 0:
        V[T[n][0]] = 2
    if V[T[n][1]] != 2:
        V[T[n][1]] = 1
    sol(T[n][1]-1)

for i in range(M):
    sol(i)

ans = 0
for i in range(N):
    if V[i] == 2 or V[i] ==0:
        ans += 1

print(ans)