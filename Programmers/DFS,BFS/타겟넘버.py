# 타겟넘버
'''
DFS 재귀함수 이용
'''
cnt = 0

def dfs(numbers,target,idx,values):
    global cnt 
    if idx == len(numbers):
        if values == target:
            cnt += 1
        return
    # 조건문을 사용하기보다 함수 파라미터에서 바로 계산!! +,- 두개뿐이기때문에
    dfs(numbers,target,idx + 1,values + numbers[idx])
    dfs(numbers,target,idx + 1,values - numbers[idx])


def solution(numbers,target):
    global cnt
    dfs(numbers,target,0,0)
    return cnt

print(solution([4, 1, 2, 1],4))