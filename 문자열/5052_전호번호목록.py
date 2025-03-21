# G4
'''
길이별로 정렬?
길이가 끝났을때 같은게 있다면?
하나씩 비교?
정렬 - 길이? 사전순?
'''
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