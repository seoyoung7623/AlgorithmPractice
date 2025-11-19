import sys
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
arr = [int(input()) for _ in range(N)]

count = [0] * (d + 1)   # 각 초밥 번호별 현재 윈도우 안 개수
distinct = 0            # 현재 윈도우 안의 서로 다른 초밥 종류 수

# 1) 처음 윈도우 [0 ~ k-1] 세팅
for i in range(k):
    if count[arr[i]] == 0:
        distinct += 1
    count[arr[i]] += 1

# 2) 쿠폰 포함해서 초기 답 계산
answer = distinct + (1 if count[c] == 0 else 0)

# 3) 슬라이딩 윈도우: 시작 인덱스를 1부터 N-1까지
for start in range(1, N):
    # 윈도우에서 빠지는 초밥 (왼쪽)
    left = arr[start - 1]
    count[left] -= 1
    if count[left] == 0:
        distinct -= 1

    # 윈도우에 새로 들어오는 초밥 (오른쪽)
    right = arr[(start + k - 1) % N]  # 원형 처리
    if count[right] == 0:
        distinct += 1
    count[right] += 1

    # 쿠폰 적용: c가 현재 윈도우에 없으면 +1
    current = distinct + (1 if count[c] == 0 else 0)

    if current > answer:
        answer = current

print(answer)