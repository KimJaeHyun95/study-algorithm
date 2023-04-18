# R, C = list(map(int, input().rstrip().split(' ')))
#
# T = [list(input().rstrip()) for _ in range(R)]
#
# # 사방 좌표 리턴
# def sol(A):
#     result = [(A[0]-1, A[1]), (A[0]+1, A[1]), (A[0], A[1]-1), (A[0], A[1]+1)]
#     del_list = []
#     for i in range(4):
#         if result[i][0] < 0 or result[i][0] >= R  or result[i][1] < 0 or result[i][1] >= C:
#             del_list.append(i)
#     for i in reversed(del_list):
#         result.pop(i)
#     return result
#
# now_location = (0, 0)
# located_list = [T[0][0]]
#
# cnt = 0
#
# def sol():
#
# while True:
#     can_location_list = sol(now_location)
#     flag = True
#     for item in can_location_list:
#         if not T[item[0]][item[1]] in located_list:
#             located_list.append(T[item[0]][item[1]])
#             now_location_list.put(item)
#
#
# print(cnt)