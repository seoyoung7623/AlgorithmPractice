# # # 7662 이중 우선순위 큐 G4

# # 최소힙의 마지막원소는 최대값이 아니다!

# import heapq
# import sys
# input = sys.stdin.readline

# def isEmpty(nums): # dict_items([('apple', 3), ('banana', 2), ('cherry', 5)])
#     for item in nums:
#         if item[1] > 0: #???
#             return False
#     return True


# T = int(input())
# for _ in range(T):
#     min_h = []
#     max_h = []
#     dic = dict() # 값 체크
#     K = int(input())
#     for i in range(K):
#         op,num = input().split()
#         num = int(num)
#         if op == 'I': # 삽입
#             if num in dic: # 원래 있는 값인 경우
#                 dic[num] += 1
#             else: # 최대힙, 최소힙
#                 dic[num] = 1
#                 heapq.heappush(min_h,num)
#                 heapq.heappush(max_h,-num) # 이거 - 찾느라 고생함..
#         elif op == 'D': # 삭제
#             if not isEmpty(dic.items()): #비어있지 않은 경우
#                 if num == 1:
#                     while -max_h[0] not in dic or dic[-max_h[0]] < 1: #최대값이 딕셔너리에 없거나, 딧셔너리에 1보다 작은경우 (없는 경우)
#                         temp = -heapq.heappop(max_h) # 최대값
#                         if temp in dic:
#                             del(dic[temp]) #한번 -1된적이 있는 것
#                     dic[-max_h[0]] -= 1 #초기삭제
#                 else:
#                     while min_h[0] not in dic or dic[min_h[0]] < 1: #한번 빠졌던 값
#                         temp = heapq.heappop(min_h) #최소값
#                         if temp in dic:
#                             del(dic[temp])
#                     dic[min_h[0]] -= 1
#     if isEmpty(dic.items()):
#         print("EMPTY")
#     else:
#         while min_h[0] not in dic or dic[min_h[0]] < 1:
#             heapq.heappop(min_h)
#         while -max_h[0] not in dic or dic[-max_h[0]] < 1:
#             heapq.heappop(max_h)
#         print(-max_h[0],min_h[0])
import sys
import heapq
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    K = int(input())
    visited = [False]*K
    minH,maxH = [],[]
    for i in range(K):
        op,num = input().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(minH,(num,i))
            heapq.heappush(maxH,(-num,i))
            visited[i] = True
        elif num == 1:
            while maxH and not visited[maxH[0][1]]: #없어졌던 것 지움
                heapq.heappop(maxH)
            if maxH: #그래야 원래 있는거 지울 수 있음
                visited[maxH[0][1]] = False
                heapq.heappop(maxH)
        else:
            while minH and not visited[minH[0][1]]:
                heapq.heappop(minH)
            if minH:
                visited[minH[0][1]] = False
                heapq.heappop(minH)
    while minH and not visited[minH[0][1]]:# 없어졌던 것 지움
        heapq.heappop(minH)
    while maxH and not visited[maxH[0][1]]:
        heapq.heappop(maxH)
    print(-maxH[0][0], minH[0][0]) if maxH and minH else print("EMPTY")
           