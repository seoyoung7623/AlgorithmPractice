import heapq;

def solution(scoville, K):
    heap = []
    answer = 0

    for i in scoville:
        heapq.heappush(heap,i)
    # 이 부분 heapq.heapify(scoville) 로 변경 가능!
    
    while heap[0]<K:
        if len(heap)>=2:
            heapq.heappush(heap, heapq.heappop(heap) + (heapq.heappop(heap))*2)
            answer +=1
        else:
            return -1

    return answer

print(solution([1, 1],7))

