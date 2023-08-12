# 4835 구간합
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # maxnum,minnum = 0,10**10
    # result = 0

    # N,M = map(int,input().split())
    # lst = list(map(int,input().split()))
    # for i in range(N-M+1):
    #     result = sum(lst[i:i+M])
    #     maxnum = max(result,maxnum)
    #     minnum = min(result,minnum)
    # print(f"#{test_case}",maxnum-minnum)
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    result = minnum = maxnum = sum(lst[0:M])
    for i in range(M,N):
        result += lst[i]
        result -=lst[i-M]
        if result < minnum:
            minnum = result
        if result > maxnum:
            maxnum = result
    print(f"#{test_case}",maxnum-minnum)

'''
구간에서 중복부분(result)의 앞에 부분은 지우고 뒷부분은 더해서 탐색하므로 탐색하는 수를 줄일수 있다. 
'''