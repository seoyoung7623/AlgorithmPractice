import sys
input = sys.stdin.readline

x = input().rstrip()
cnt = 0
answer = False
if len(x) == 1:
    if int(x)%3 == 0:
        answer = True
else:
    while 1:
        total = sum(list(map(int,x)))
        cnt += 1
        x = str(total)
        if len(x) == 1:
            if total%3 == 0:
                answer = True
            break
print(cnt)
if answer:
    print('YES')
else:
    print('NO')