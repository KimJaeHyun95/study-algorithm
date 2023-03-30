T = int(input())

# b: 배추위치
def sol(b):
    U[b[0]][b[1]] = 0
    if U[b[0]-1][b[1]]:
        sol([b[0]-1, b[1]])
    if U[b[0]+1][b[1]]:
        sol([b[0]+1, b[1]])
    if U[b[0]][b[1]-1]:
        sol([b[0], b[1]-1])
    if U[b[0]][b[1]+1]:
        sol([b[0], b[1]+1])



for aaaa in range(T):
    M, N, K = list(map(int, input().rstrip().split(' ')))
    B = [list(map(int, input().rstrip().split(' '))) for i in range(K)]
    U = [[0 for _ in range(N+2)] for _ in range(M+2)]
    for i in range(K):
        U[B[i][0]+1][B[i][1]+1] = 1
    print(*U, sep='\n')
    print()
    cnt = 0
    for i in range(1, M+1):
        for j in range(1, N+1):
            if U[i][j]:
                cnt += 1
                sol([i, j])
                print(*U, sep='\n')
                print()
    print(cnt)
