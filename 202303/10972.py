N = int(input())

A = list(map(int, input().rstrip().split()))


V = []
T = []


def sol():
    if len(T) == N:
        V.append(T[:])
        return
    else:
        for i in range(1, N+1):
            if i not in T:
                T.append(i)
                sol()
                T.pop()


sol()

for i in range(len(V)):
    if A == V[i]:
        if i != len(V)-1:
            print(V[i+1])
        else:
            print(-1)