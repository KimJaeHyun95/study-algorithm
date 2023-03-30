N = int(input())

T = [list(map(int, input().rstrip().split(' '))) for i in range(N)]

def sol(lst):

    min_index = 0
    second_min_index = 1

    if lst[1] < lst[0]:
        min_index, second_min_index = 1, 0

    if lst[2] < lst[min_index]:
        second_min_index = min_index
        min_index = 2
    elif lst[2] < lst[second_min_index]:
        second_min_index = 2

    return min_index, second_min_index
a, b = 3, 3
ans = [0, 0]
for i in range(N):
    A = sol(T[i])
    if A[0] != a:
        if A[1] != a:
            ans = [ans[0]+T[i][A[0]], ans[0]+T[i][A[1]]]
        else:
            ans = [ans[0]+T[i][A[0]], ans[1]+T[i][A[1]]]
    else:
        if A[1] != a:
            ans = [ans[1]+T[i][A[0]], ans[0]+T[i][A[1]]]
        else:
            ans = [ans[1]+T[i][A[0]], ans[1]+T[i][A[1]]]
    a = A[0]
    b = A[1]
    print(ans)
print(min(ans))