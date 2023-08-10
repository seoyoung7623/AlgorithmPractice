#6485 삼성시의 버스노선 D3 https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWczm7QaACgDFAWn&
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    lst = [0]*(5001)
    N = int(input())
    for n in range(N):
        A,B = map(int,input().split())
        for i in range(A,B+1):
            lst[i] += 1
    P = int(input())
    result = [0]*(P)
    for j in range(P):
        C = int(input())
        result[j] = lst[C]

    print(f'#{test_case}',*result)
