# 수묶기 G4
'''
묶은 수의 최대 합
-1,2,1,3 곱이 최대가 되어야한다. 
묶는건 두 수만 가능

0을 기준으로
만약 0을 묶으면 양의 합보다 작아짐
만약 0은 음수랑 묶으면 수를 음수를 상쇄할 수 있음

1을 기준으로
2*1보다 2+1이 더 큼
1은 모두 합으로 처리한다.
    1의 개수만큼 추가해준다.

음수
0은 가장 작은 음수와 곱해야한다. (x) 가장 작은 음수는 음수와 곱하는게 수가 더 크다.
음수들은 서로 곱하면 수를 키울 수 있음
⭐️ 음수끼리곱>음수*0 따라서 0음 남은 가장큰 음수와 곱해준다.
'''
'''
범위 50개 -1000 ~ 1000
'''

'''
✅ 해결 풀이
3개의 그룹으로 나눌수있다.(양수,1,0과 음수)
0은 무조건 음수와 곱하는것이 나음 0음 음수그룹으로 생각한다.
그룹을 나눠서 아예 따로 계산하기

🤔 이 문제가 그리디인 이유?
현재 선택이 항상 최적의 해를 보장해야함
'''
N = int(input())
lst = [int(input()) for _ in range(N)]

positive = []
negative = []
ones = 0
zero = 0

for num in lst:
    if num>1:
        positive.append(num)
    elif num == 1:
        ones += 1
    elif num == 0:
        zero += 1
    else:
        negative.append(num)

positive.sort(reverse=True)
negative.sort()
result = 0

for i in range(0,len(positive)-1,2):
    result += (positive[i] * positive[i+1])
if len(positive) % 2 == 1:
    result += positive[-1]

for i in range(0,len(negative)-1,2):
    result += (negative[i]*negative[i+1])
if len(negative) % 2 == 1:
    if zero == 0:
        result += negative[-1]
result += ones
print(result)