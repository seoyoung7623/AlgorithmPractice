# 2531 회전초밥 S1
'''
각 초밥 번호별로 개수를 저장한다. count리스트
unique: 현재 서로 다른 초밥의 개수 저장
슬라이딩 윈도우로 지나간건 count배열의 값을빼고, 앞에는 count배열에 값을 넣는 형식으로 진행가능!!
'''
N,d,k,c = map(int,input().split())
arr = list(int(input()) for _ in range(N))

count = [0]*(d+1)
unique = 0

for i in range(k):
    if count[arr[i]] == 0:
        unique += 1
    count[arr[i]] += 1

max_unique = unique + (1 if count[c] == 0 else 0)

for i in range(N):
    left = arr[i]
    count[left] -= 1
    if count[left] == 0:
        unique -= 1
    
    right = arr[(i+k)%N]
    if count[right] == 0:
        unique += 1
    count[right] += 1

    max_unique = max(max_unique,unique + (1 if count[c] == 0 else 0))

print(max_unique)