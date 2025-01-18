# 7795 먹을 것인가 먹힐 것인가 S3
'''
투포인터 힌트가 없었다면 완탐했을듯.. 
정렬을하면 해당 인덱스만큼의 작은수가 존재함. 두 포인터 크기를 비교한다.
완탐: O(N^2)
투포인터: O(N)
'''

T = int(input())
for test_case in range(T):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B.sort()

    i,j = 0,0
    count = 0

    while i<N:
        if A[i]<=B[j]:
            i+=1
            count += j
        elif A[i] > B[j]:
            if j == M-1:
                count += j+1
                i+=1
                continue
            j+=1
    
    print(count)