import sys
input = sys.stdin.readline

T = int(input())
for test_case in range(T):
    n = int(input())
    lst = list(input().rstrip() for _ in range(n))
    lst.sort(key=lambda x:(x,len(x)))
    for i in range(1,len(lst)):
        if lst[i].startswith(lst[i-1]):
            print('NO')
            break
    else:
        print('YES')