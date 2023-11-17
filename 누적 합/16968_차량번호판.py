# 16968 차량번호판 B1
'''
중복이 3개 이상인 경우 10, 9, 8 이 아니라 10,9,9!
'''
ans = input()
if ans[0] == 'c':
    result = 26
else:
    result = 10
for i in range(1,len(ans)):
    if ans[i] == 'c':
        if ans[i-1] == 'c':
            result *= 25
        else:
            result *= 26
    else:
        if ans[i-1] == 'd':
            result *= 9
        else:
            result *= 10

print(result)
