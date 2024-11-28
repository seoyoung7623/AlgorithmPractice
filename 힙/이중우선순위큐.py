# # 이중우선순위큐
'''
1. 최대값 힙큐, 최소값 힙큐 두개를 만들어서 최대, 최소를 구함
'''
import heapq
def solution(operations):
    answer = []
    min_h = []
    max_h = []
    for op in operations:
        i,num = op.split()
        if i == 'I':
            heapq.heappush(min_h,int(num))
            heapq.heappush(max_h,-int(num))
        else:
            if min_h:
                if num == '-1':
                    value=heapq.heappop(min_h)
                    max_h.remove(-value)
                else: # 최대값 삭제
                    value=heapq.heappop(max_h)
                    min_h.remove(-value)
    answer = [-heapq.heappop(max_h) if max_h else 0,heapq.heappop(min_h) if min_h else 0]     
    return answer
print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))


'''
2.우선순위큐에서 큰 수를 뽑을수 있는 함수이용
heapq.nlargest(n, list) : 리스트에서 가장 큰 수 n개를 뽑을 수 있는 함수
heap = heapq.nlargest(len(heap), heap)[1:]
'''
import heapq

def solution(operations):
    answer = []
    heap = []
    for op in operations:
        i,num = op.split()
        if i == 'I':
            heapq.heappush(heap,int(num))
        else:
            if heap:
                if num == '-1':
                    heapq.heappop(heap)
                else:
                    heap = heapq.nlargest(len(heap),heap)[1:] # 결과가 리스트로 나오기 때문에 주의
                    heapq.heapify(heap)
    if heap:
        answer = [heapq.nlargest(1,heap)[0],heapq.heappop(heap)]
    else:
        answer = [0,0]
    return answer

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))