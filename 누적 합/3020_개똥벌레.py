# 3020 개똥벌레 G5
# 누적합문제
'''
시간초과

누적합을 어떻게 사용할것인가?
특정 높이 이상 이하에서 있는 장애물 개수를 빠르게 구한다.
'''
import sys
input = sys.stdin.readline

N, H = map(int, input().split())
stone = list(int(input()) for _ in range(N))

# 석순과 종유석 분리
floor = stone[::2]
ceiling = stone[1::2]


# 높이별 석순, 종유석 누적합 배열 계산
floor_count = [0] * (H+1)
ceiling_count = [0] * (H+1)

for f in floor:
    floor_count[f] += 1
for c in ceiling:
    ceiling_count[H-c+1] += 1

for i in range(H-1,0,-1):
    floor_count[i] += floor_count[i+1]
for i in range(2,H+1):
    ceiling_count[i] += ceiling_count[i-1]

sum = []
for i in range(1,H+1):
    sum.append(floor_count[i]+ceiling_count[i])
print(min(sum),sum.count(min(sum)))
