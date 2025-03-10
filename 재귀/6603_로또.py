# S2
'''
조합 combbinations
'''
from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    k = list(map(int,input().split()))
    if k == [0]:
        break
    k = k[1::]
    answer = sorted(list(combinations(k,6)))

    for i in range(len(answer)):
        print(*answer[i])
    print()