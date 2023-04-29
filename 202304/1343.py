A = input()

B = A.split('.')

print(B)

ans = ''

for item in B:
    len_item = len(item)
    if len_item % 2 == 0:
        AAAA_cnt = len_item // 4
        BB_cnt = len_item % 4
        ans += 'AAAA'*AAAA_cnt + 'BB'*(BB_cnt//2)
    else:
        ans = -1
        break

if ans == -1:
    print(ans)
else:
    for i in range(len(A)):
        if A[i] == '.':
            ans = ans[:i] +'.' + ans[i:]

    print(ans)