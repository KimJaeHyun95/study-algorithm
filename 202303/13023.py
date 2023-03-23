N, M = list(map(int, input().strip().split(' ')))

T = [list(map(int, input().strip().split(' '))) for i in range(M)]

U = {i: [] for i in range(N)}

for item in T:
    U[item[0]].append(item[1])
    U[item[1]].append(item[0])

flag = False

V = []

def sol(n):
    global flag
    if flag:
        return
    if len(V) == 5:
        flag = True
        return
    for _item in U[n]:
        if _item not in V:
            V.append(_item)
            sol(_item)
            V.pop()


for i in range(M):
    V = [T[i][0], T[i][1]]
    sol(T[i][1])


if flag:
    print(1)
else:
    print(0)