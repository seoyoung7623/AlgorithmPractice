'''
어떠한 수를 써서라도 만들수 없는 경우? 큐1->큐2로 같은 길이 만큼 준경우
큐1이 더 크면 큐2
'''
from collections import deque

def solution(queue1, queue2):
    total = sum(queue1) + sum(queue2)
    if total%2 != 0:
        answer = -1
        return answer
    total = total//2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    answer = 0
    while 1:
        if sum1 < total:
            num = queue2.popleft()
            queue1.append(num)
            sum1 += num
            sum2 -= num
            answer += 1
        elif sum2 < total:
            num = queue1.popleft()
            queue2.append(num)
            sum2 += num
            sum1 -= num
            answer += 1
        else:
            break
        if answer > len(queue1) + len(queue2):
            answer = -1
            break
    return answer
print(solution([1, 2, 1, 2],[1, 10, 1, 2]))