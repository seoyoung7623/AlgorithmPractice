# 백만장자 프로젝트 D2
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    maxValue = 0
    sum = 0
    for i in arr[::-1]:
        if i > maxValue:
            maxValue = i
        else:
            sum += maxValue - i
    print(f"#{test_case} {sum}")