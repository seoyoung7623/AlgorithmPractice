#1326 폴짝폴짝
# from collections import deque


# totalnum = int(input())
# road = list(map(int,input().split()))
# a,b = map(int,input().split())
# queue = deque()
# cnt = 0

# def bfs(s): #현재인덱스, 인덱스 값 배수
#     queue.append(s)
#     for i in range(-10,10):
#         if 0<=s+road[s]*i<len(road):
#             cnt +=1
#             bfs(s+road[s]*i)
#         if s+road[s]*i == b:
#             break


# bfs(a) 


from collections import deque

def bfs(a, b, bridge, N):
    q = deque()
    q.append(a-1) #처음 인덱스 추가
    check = [-1]*N #-1을 총 길이만큼 추가
    check[a-1] = 0 #첫인덱스 확인
    while q:
        node = q.popleft()

        #현재 다리에서 앞으로 건너는 경우
        for n in range(node, N, bridge[node]):
            if check[n] == -1: #확인 안됐다면
                q.append(n)
                check[n] = check[node] + 1 #확인됨 지나 갈때마다 계속 +1
                if n == b-1: #확인한 인덱스가 목적지
                    return check[n]

        #현재 다리에서 뒤로 건너는 경우
        for n in range(node, -1, -bridge[node]): # -1 주의 0까지의 정수 범위를 반환
            if check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
                if n == b-1:
                    return check[n]
    return -1

N = int(input()) 
bridge = list(map(int, input().split()))
a, b = map(int, input().split())
print(bfs(a, b, bridge, N))