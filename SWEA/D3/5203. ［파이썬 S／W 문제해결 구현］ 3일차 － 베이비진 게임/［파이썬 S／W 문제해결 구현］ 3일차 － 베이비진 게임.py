'''
연속 숫자 확인 어떻게 할지
set을 정렬 sorted하면 리스트로 반환
빈도 수로 측정
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    arr = list(map(int,input().split()))
    ca = [0] * 10
    cb = [0] * 10
    winner = 0
    
    def win(arr):
        if any(c>= 3 for c in arr):
            return True
        for i in range(8):
            if arr[i] and arr[i+1] and arr[i+2]:
                return True
        return False
    
    for i,v in enumerate(arr):
        if i % 2 == 0:
            ca[v] += 1
            if i >= 4 and win(ca):
                winner = 1
                break
        else:
            cb[v] += 1
            if i >= 5 and win(cb):
                winner = 2
                break

    print(f"#{test_case} {winner}")   
             