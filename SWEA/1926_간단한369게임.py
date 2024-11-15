# 1926 간단한 369 게임
'''
N이 10이상 1000 이하이기때문에 3자리만 검사하면됨
만약 1자리인데 100으로 나누면?

2. replace() 13 -> 1- 이렇게 처리되는 문제
'''

# 자리수 나누기
n = int(input())
number = []
for i in range(1,n+1): # 1,n+1
    if i < 10 and (i%10) in (3,6,9):
        i = '-'
    elif 10 <= i < 100:
        cnt = 0
        if (i//10) in (3,6,9):
            cnt += 1
        if (i%10) in (3,6,9):
            cnt += 1
        if cnt != 0:
            i = '-'*cnt
    elif 100 <= i < 1000:
        cnt = 0
        if (i // 100) in (3,6,9):
            cnt += 1
        if ((i%100) // 10) in (3,6,9):
            cnt += 1
        if (i%10) in (3,6,9):
            cnt += 1
        if cnt != 0:
            i = '-' * cnt
    number.append(str(i))
print(' '.join(number))

# 자리수를 str로 변경해서 이중 리스트돌기
n = int(input())
clab = ['3','6','9']
for i in range(1, n+1):
    count = 0
    for j in str(i):
        if j in clab:
            count += 1
    if count != 0:
        i = '-'*count
    print(i,end= ' ')

