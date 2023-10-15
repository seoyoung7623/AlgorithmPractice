# # 7662 이중 우선순위 큐 G4

# 최소힙의 마지막원소는 최대값이 아니다!

import heapq
import sys
input = sys.stdin.readline

def isEmpty(nums):
    for item in nums:
        if item[1] > 0: #???
            return False
    return True


T = int(input())
for _ in range(T):
    min_h = []
    max_h = []
    dic = dict() # 값 체크
    K = int(input())
    for i in range(K):
        op,num = input().split()
        num = int(num)
        if op == 'I': # 삽입
            if num in dic: # 원래 있는 값인 경우
                dic[num] += 1
            else: # 최대힙, 최소힙
                dic[num] = 1
                heapq.heappush(min_h,num)
                heapq.heappush(max_h,-num) # 이거 - 찾느라 고생함..
        elif op == 'D': # 삭제
            if not isEmpty(dic.items()): #비어있지 않은 경우
                if num == 1:
                    while -max_h[0] not in dic or dic[-max_h[0]] < 1:
                        temp = -heapq.heappop(max_h)
                        if temp in dic:
                            del(dic[temp])
                    dic[-max_h[0]] -= 1
                else:
                    while min_h[0] not in dic or dic[min_h[0]] < 1:
                        temp = heapq.heappop(min_h)
                        if temp in dic:
                            del(dic[temp])
                    dic[min_h[0]] -= 1
    if isEmpty(dic.items()):
        print("EMPTY")
    else:
        while min_h[0] not in dic or dic[min_h[0]] < 1:
            heapq.heappop(min_h)
        while -max_h[0] not in dic or dic[-max_h[0]] < 1:
            heapq.heappop(max_h)
        print(-max_h[0],min_h[0])
