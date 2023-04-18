N = int(input())
A = list(map(int, input().rstrip().split(' ')))
M = int(input())
B = list(map(int, input().rstrip().split(' ')))

A.sort()

for item in B:
    if item not in A:
        print(0)
    else:
        cnt = 1
        for i in range(A.index(item)+1, M):
            if A[i] == item:
                cnt += 1
            else:
                break
        print(cnt)
