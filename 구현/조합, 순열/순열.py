# 순열 라이브러리 없이 구현
def perm(arr):
    result = []
    def backtrack(start):
        if start == len(arr):
            result.append(arr[:])
            return
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start] #3,2, 자리 바뀜
            backtrack(start + 1)
            arr[start],arr[i] = arr[i], arr[start]
    backtrack(0)
    return result

print(perm([1,2,3]))