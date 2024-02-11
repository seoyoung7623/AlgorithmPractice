# 다리를 지나는 트럭 Lv2

# 1. 리스트 이용
# def solution(bridge_length, weight, truck_weights):
#     time = 0
#     stack = [0]*bridge_length
#     while len(truck_weights) != 0:
#         time += 1
#         stack.pop(0)
#         if sum(stack) + truck_weights[0] <= weight:    
#             stack.append(truck_weights.pop(0))
#         else:
#             stack.append(0)
            
#     time += bridge_length #브릿지 길이만큼
#     return time
# print(solution(2,10,[7,4,5,6]))

# 2. deque 이용
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    q = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    current_weight = 0
    while len(truck_weights) != 0:
        time += 1
        current_weight -= q.popleft()
        if current_weight + truck_weights[0] <= weight:    # sum때문에 시간초과
            current_weight += truck_weights[0]
            q.append(truck_weights.popleft())
        else:
            q.append(0)
            
    time += bridge_length #브릿지 길이만큼
    return time
