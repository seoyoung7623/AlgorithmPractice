# 프로세스 Lv2
'''
스택이용
- pop(0) 은 popleft()와 같음
'''
# 내 풀이
# from collections import deque

# def solution(priorities, location):
#     answer = 0
#     q =  [[p,i] for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         if q[0][0] == max(q,key=lambda x:x[0]) and q[0][1] == location:
#             answer += 1
#             break
#         if q[0][0] == max(q,key=lambda x:x[0]): # 그냥 max 람다가 안되는듯?
#             answer += 1
#             q.pop(0)
#         else:
#             q.append(q.pop(0))
#     return answer
# print(solution([1, 1, 9, 1, 1, 1],0))

# 참고풀이
def solution(priorities,location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)] #1. enumerate 함수 이용
    while True:
        cur = queue.pop(0) # 2. 0번째를 꺼냄
        if any(cur[1] < q[1] for q in queue): # 큐를 모두 돌아 이것보다 작은것은 계속 넣고 뺀다.
            # 3. max대신 any함수를 큐 전체에서 작은 값들을 모두 fifo한다.
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location: # 가장 큰 값중에서 location값을 찾아 리턴한다.
                return answer
    