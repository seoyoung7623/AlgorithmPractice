#2805 나무자르기
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
tree = list(map(int,input().split()))
start,end = 1,max(tree)

while start <= end: #주의
    min = (start+end) //2

    cnt = 0 #한 루프당 막대 길이를 지정한 경우를 나타내기때문에 루프안에 필요!
    for i in tree:
        if min < i:
            cnt += (i-min)
        # if cnt >= m:
        #     print(cnt)
        #     break
    if cnt < m: # =삭제! 중요
        end = min-1
    else: # cnt=m인경우 start가 min+1이 되서 루프를 실행하지않고 탈출한다.
        start = min+1
print(end) #중요 
