# 2217 로프 S4
'''
<초기 접근>
2개 10, 15
들수있는 최대 중량
20, 10,10
최소값* N

<그리디 이용>
3개 10,30,60
30이 아닌 30,30 총 60
3개 10,30,70
60이 아닌 70으로 하나
n 10^5 시간가능
1. 가장 긴 로프 하나
2. 이전값의 2개 최대값구하기
'''
N = int(input())
arr = []
answer = 0
for _ in range(N):
    arr.append(int(input()))
arr.sort(reverse=True)
for i,num in enumerate(arr):
    answer =  max((i+1)*num,answer)

print(answer)