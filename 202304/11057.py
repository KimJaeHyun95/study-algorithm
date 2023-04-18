N = int(input())

V = [1 for _ in range(10)]
T = [0 for _ in range(10)]

for _ in range(N-1):
    for i in range(10):
        for j in range(i, 10):
            T[j] += V[i]
    V = T[:]
    T = [0 for _ in range(10)]


print(sum(V)%10007)