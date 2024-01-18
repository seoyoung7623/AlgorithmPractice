# 2696 중앙값 구하기 G5
import sys
import heapq

input = sys.stdin.readline

def solution(data):
    smallh = []
    bigh = []
    middle = data[0]
    result = [middle]

    for idx, val in enumerate(data[1:],1):
        if val > middle:
            heapq.heappush(bigh,val)
        else:
            heapq.heappush(smallh,(-val,val))
        
        if idx % 2 == 0:
            if len(smallh) < len(bigh):
                heapq.heappush(smallh,(-middle,middle))
                middle = heapq.heappop(bigh)
            elif len(smallh) > len(bigh):
                heapq.heappush(bigh,middle)
                middle = heapq.heappop(smallh)[1]
            result.append(middle)
    print(len(result))

    for i in range(len(result)):
        if i != 0 and (i+1) % 10 == 1:
            print()
        print(result[i],end=' ')
    print()

t = int(input())
for i in range(t):
    m = int(input())
    data = []
    # 10개 단위로 입력받기
    if m % 10 == 0:
        for _ in range(m//10):
            data.extend(list(map(int,input().split(' '))))
    else:
        for _ in range(m//10+1):
            data.extend(list(map(int,input().split(' '))))
    
    solution(data)