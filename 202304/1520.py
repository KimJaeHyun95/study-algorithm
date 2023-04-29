N, M = list(map(int, input().rstrip().split(' ')))

T = [[10001] * (M + 2)]  # 첫 행에 0 추가

[T.append(list(map(int, ('10001 ' + input() + ' 10001').rstrip().split(' ')))) for _ in range(N)]
T.append([10001] * (M + 2))

dp = [[0 for _ in range(M+2)] for _ in range(N+2)]

dp[1][1] = 1

location = [(1, 1)]

def go(x, y):
    if x == N and y == M:
        return
    h = T[x][y]
    v = dp[x][y]
    dp[x][y] = 0
    if T[x-1][y] < h:
        dp[x-1][y] += v
    if T[x][y-1] < h:
        dp[x][y-1] += v
    if T[x+1][y] < h:
        dp[x+1][y] += v
    if T[x][y+1] < h:
        dp[x][y+1] += v

while True:
     temp_location = location[:]
     location = []
     for item in temp_location:
         go(item)