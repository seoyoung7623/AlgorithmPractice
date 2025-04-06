n,m = map(int,input().split())
if m != 0:
    arr = set(map(int,input().split()))
else:
    arr = set()
answer = 0

def backtracking(length,used_digits):
    global answer
    if length == n:
        if arr.issubset(used_digits):
            answer += 1
        return
    for i in range(10):
        new_digits = used_digits.copy() # 새로 갱신 이렇게하면 set집할이라도 모든 수를 추가할수있음
        new_digits.add(i)
        backtracking(length+1,new_digits)

backtracking(0,set())
print(answer)