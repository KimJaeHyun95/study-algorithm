N, S = list(map(int, input().rstrip().split(' ')))
T = list(map(int, input().rstrip().split(' ')))

V = []
cnt = 0

def cal():
    s = 0
    for item in V:
        s += T[item]
    return s

def sol():
    global cnt
    if cal() == S:
        cnt += 1
    if len(V) == 0:
        l = - 1
    else:
        l = V[len(V)-1]

    for i in range(l+1, N):
        V.append(i)
        sol()
        V.pop()

sol()

if S == 0:
    cnt -= 1

print(cnt)