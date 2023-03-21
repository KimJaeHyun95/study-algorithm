N = int(input())
T = list(map(int, input().rstrip().split(' ')))

V = []

Max = 0

def cal():
    s = 0
    for i in range(N-1):
        s += abs(T[V[i]]-T[V[i+1]])
    return s



def sol():
    global Max
    if len(V) == N:
        m = cal()
        if Max < m:
            Max = m
        return
    else:
        # 동일한 값이 들어 올 수도 있으므로 인덱스를 키 값으로 한다.
        for i in range(N):
            if i not in V:
                V.append(i)
                sol()
                V.pop()


sol()
print(Max)