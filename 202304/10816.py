N = int(input())
num_list = list(map(int, input().rstrip().split(' ')))
M = int(input())
f_list = list(map(int, input().rstrip().split(' ')))

num_dict = {item: 0 for item in set(num_list)}

for item in num_list:
    num_dict[item] += 1

for item in f_list:
    try:
        print(num_dict[item], end = ' ')
    except KeyError:
        print(0, end = ' ')