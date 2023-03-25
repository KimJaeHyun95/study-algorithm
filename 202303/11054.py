N = int(input())

T = list(map(int, input().rstrip().split(' ')))

V = []

def cal():
    if len(V) < 3:
        return False
    flag = 0
    for i in range(len(V)):
        if i == len(V) - 1:
            if flag == 1:
                return True
            else:
                return False
        if T[V[i]] == T[V[i + 1]]:
            return False
        if flag == 0:
            if T[V[i]] < T[V[i+1]]:
                continue
            else:
                flag = 1
        elif flag == 1:
            if T[V[i]] < T[V[i+1]]:
                return False
            else:
                continue


ans = 0
def sol(n):
    global ans
    for i in range(n, N):
        if i not in V:
            V.append(i)
            if cal() or len(V) < 3:
                if ans < len(V):
                    ans = len(V)
                sol(i)
                V.pop()
            else:
                V.pop()

sol(0)
print(ans)