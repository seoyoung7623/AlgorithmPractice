# G5
'''
최소강의실의 개수
끝나는 시간을 기준으로 정렬
1,3/3,5
2,4/4,6
3,6

끝나는 시간을 저장
N<2e5

이분탐색이 적절하지 않은 이유
rooms.sort()가 매번 실행됨 → O(N log N)
끝나는 시간을 기준으로 배정하면 최소한의 강의실을 만족할 수 없음
'''
# import sys
# input = sys.stdin.readline
# N = int(input())
# rooms = []
# times = [list(map(int,input().split())) for _ in range(N)]
# times.sort(key=lambda x:(x[1]))

# for start,end in times:
#     if rooms:
#         rooms.sort()
#         left = 0
#         right = len(rooms)-1
#         while left<=right:
#             mid = left + (right-left) // 2
#             if start >= rooms[mid]:
#                 left = mid + 1
#                 index = mid
#             elif start < rooms[mid]:
#                 right = mid - 1
#         if right == -1 or left == len(rooms):
#             rooms.append(end)
#         else:
#             rooms[index] = end
#     else:
#         rooms.append(end)
# print(len(rooms))

'''
그리디 + 우선순위큐
끝나는 시간이 가장 빠른것보다 시작이간이 더 빠르면 힙에 추가해줌

놓친 부분: 강의 시작시간을 기준으로 정렬
강의를 가능한한 한 강의실에 배정하는것이 중요 따라서 시작이 빠른 강의부터 처리
'''

import heapq
import sys
input = sys.stdin.readline
N = int(input())
rooms = []
times = [list(map(int,input().split())) for _ in range(N)]
times.sort()

for start,end in times:
    if not rooms:
        heapq.heappush(rooms,end)
        continue
    if rooms[0] <= start:
        heapq.heappop(rooms)
    heapq.heappush(rooms,end)
print(len(rooms))

