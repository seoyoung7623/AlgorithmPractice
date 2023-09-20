# 순열 라이브러리 없이 구현
def perm(arr):
    result = []
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start] # 스왑을 통해 원소의 위치를 변경 
            backtrack(start + 1)
            arr[start],arr[i] = arr[i], arr[start] # 백트래킹을 나오면 바뀐 위치를 이전 상태로 복구
    backtrack(0)
    return result

print(perm([1,2,3]))