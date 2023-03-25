N =int(input())

T = list(map(int, input().rstrip().split(' ')))

V = []


def cal():
    sum = 0
    for i in V:
        sum += T[i]
    return sum

ans = set()

a = 0

def sol():
    global a
    if not V:
        l = a
        a += 1
    else:
        l = V[len(V)-1]
    for i in range(l, N):
        if i not in V:
            V.append(i)
            ans.add(cal())
            sol()
            V.pop()

sol()

cnt = 1
while cnt in ans:
    cnt +=1

print(cnt)