N = int(input())

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

for item in V:
    print(*item)