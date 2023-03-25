N = int(input())
M = int(input())

T = [list(map(int, input().rstrip().split(' '))) for i in range(M)]

map = {i: [] for i in range(N+1)}

for item in T:
    map[item[0]].append(item[1])
    map[item[1]].append(item[0])

V = []

def sol(n):
    for item in map[n]:
        if item not in V:
            V.append(item)
            sol(item)

sol(1)

print(len(V)-1)