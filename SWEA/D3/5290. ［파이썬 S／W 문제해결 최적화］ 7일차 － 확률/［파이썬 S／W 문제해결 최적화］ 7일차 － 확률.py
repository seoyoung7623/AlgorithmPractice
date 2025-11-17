'''
3자리 다른 숫자 9 * 9 * 8 / 9 * 10 * 10 전체 
'''

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    total = 9
    M = 9
    for i in range(N-1):
        total *= 10
        M *= (9-i)
    print(f"#{test_case} {M/total:.5f}")