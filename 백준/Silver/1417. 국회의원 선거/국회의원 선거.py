import heapq
N = int(input())
dasom = int(input())
dasom_copy = dasom
arr = [-int(input()) for _ in range(N-1)]
heapq.heapify(arr)

while arr and -arr[0] >= dasom:
    vote = -heapq.heappop(arr)
    if vote >= dasom:
        vote -= 1
        dasom += 1
        heapq.heappush(arr,-vote)
print(dasom-dasom_copy)