#1920 수찾기 이분탐색

n1 = int(input())
n1list = list(map(int,input().split()))
n2 = int(input())
n2list = list(map(int,input().split()))
n1list.sort
# for i in n2list:
#     if i in n1list:
#         print(1)
#     else:
#         print(0) 
# 시간초과에러

def binary(l,N,start,end):
    if start > end:
        return 0
    m = (start + end)//2
    if l == N[m]:
        return 1
    elif l < N[m]:
        return binary(l,N,start,m-1) #작은값인경우 end값이 중간이하
    else:
        return binary(l,N,m+1,end)

for i in n2list:
    start = 0
    end = len(n1list)-1
    print(binary(i,n1list,start,end))