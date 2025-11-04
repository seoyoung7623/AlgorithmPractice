T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
from collections import deque

for test_case in range(1, T + 1):
    N,M = map(int,input().split())
    arr = list(map(int,input().split()))
    q = deque(arr)
    q.rotate(-M)
    print(f"#{test_case} {q[0]}")