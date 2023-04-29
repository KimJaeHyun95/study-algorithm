N = int(input())

T = [list(map(int, input().rstrip().split(' '))) for i in range(N)]

V = T[0][:]

for i in range(1, N):
    temp_T = T[i]
    temp_V = [0, 0, 0]
    for j in range(3):
        temp_V[j] = min(V[(j+1)%3], V[(j+2)%3])
    V = [v + t for v, t in zip(temp_V, temp_T)]

print(min(V))