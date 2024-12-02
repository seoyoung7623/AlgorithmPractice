# 2003 수들의 합2 S4
'''
누적합을 구하고 그 누적합들이 M이 되는 조합을 구한다.
모든 누적합을 구해야하나?
누적합은 오른쪽으로 갈수록 커지는 숫자
포인터를 이용해 수가 왼쪽을 옮기자.

N 10^4 M 10^9
'''

N,M = map(int,input().split())
arr = list(map(int,input().split()))
left, right = 0,0
cnt = 0
sum = 0

while 1:
    # 합이 M에 미도달
    if sum <= M:
        if right == N:
            break
        sum += arr[right]
        right += 1
    # 합이 M이상일때
    else:
        sum -= arr[left]
        left += 1
    if sum == M:
        cnt += 1
print(cnt)
    
