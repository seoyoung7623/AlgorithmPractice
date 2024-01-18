# # 2696 중앙값 구하기 G5
'''
힙큐를 이용한 중간값을 찾는 문제
중간값을 설정하고, 홀수의 중간값보다 작은 값들과 큰 값들의 수가 다를 경우 중간값 설정을 다시 해줌
따라서, 중간값은 작은값들과 큰 값들의 수가 같을때가 중간 값이다.
'''
import heapq
import sys
input = sys.stdin.readline

def solution(data):
    smallh = []
    bigh = []
    mid = data[0]
    result = [mid]

    for idx,val in enumerate(data[1:],1):
        if mid < val :
            heapq.heappush(bigh,val)
        else:
            heapq.heappush(smallh,(-val,val))
        
        if idx % 2 == 0:
            if len(smallh) < len(bigh):
                heapq.heappush(smallh, (-mid, mid))
                mid = heapq.heappop(bigh)
            elif len(smallh) > len(bigh):
                heapq.heappush(bigh, mid)
                mid = heapq.heappop(smallh)[1]
            result.append(mid)
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
    # 10개 단위로 입력받음
    if m % 10 == 0:
        for _ in range(m//10):
            data.extend(list(map(int,input().split(' '))))
    else:
        for _ in range(m//10+1):
            data.extend(list(map(int,input().split(' '))))
    solution(data)
