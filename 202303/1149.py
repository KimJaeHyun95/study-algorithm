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

ans = [0, 0, 0]
for i in range(N):
    A = sol(T[i])
    

    print(ans)
print(min(ans))