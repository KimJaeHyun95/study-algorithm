N = int(input())

T = list(map(int, input().rstrip().split(' ')))

V = []

D = []


ans = []

def cal():
    sum = 0
    for i in V:
        sum += T[i]
    return sum

def sol():
    ans.append(cal())
    if len(V) == 0:
        l = 0
    else:
        l = V[len(V)-1]+1
    for i in range(l, N):
        if i not in V:
            V.append(i)
            sol()
            V.pop()

sol()

cnt = 1

while cnt in ans:
    cnt += 1

print(cnt)