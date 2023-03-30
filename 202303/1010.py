T = int(input())

def fac(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fac(n-1)

for _ in range(T):
    N, M = list(map(int, input().rstrip().split(' ')))
    print((fac(M)//fac(M-N))//fac(N))