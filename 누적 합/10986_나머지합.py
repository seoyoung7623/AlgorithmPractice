# 10986 나머지 합 G3
'''
누적합의 차의 나머지 공식
같은 나머지들의 차는 나머지가 0을 이용한 조합 개수
'''

N,M = map(int,input().split())
arr = list(map(int,input().split()))

remain_arr = [0]*M
prefix_sum = 0
count = 0
for num in arr:
    prefix_sum += num
    remainder = prefix_sum % M

    if remainder == 0:
        count += 1
    remain_arr[remainder]+=1

for r in remain_arr:
    if r >= 2:
        count += r*(r-1)//2
print(count)
    

