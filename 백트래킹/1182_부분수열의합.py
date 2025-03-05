# S2 ⭐️⭐️⭐️
'''
부분수열: 연속적이지 않아도 되며 원소의 순서를 유지해야한다.
연속인 수 아님! 
✅ 백트레킹
원소를 포함,미포함 선택하여 나아간다.
수열 문제
'''
N,S = map(int,input().split())
arr = list(map(int,input().split()))
answer = 0

def backtracking(idx,total):
    global answer
    if idx >= N:
        return
    total += arr[idx]
    if total == S:
        answer += 1
    backtracking(idx+1,total)
    backtracking(idx+1,total-arr[idx]) #숫자를 다시 빼서 취소

backtracking(0,0)
print(answer)

