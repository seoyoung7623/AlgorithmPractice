T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    
    def quick(arr):
        #print(arr)
        if len(arr) <= 1:
            return arr
        
       	pivot = arr[0]
        #print(pivot)
        left = [arr[i] for i in range(len(arr)) if arr[i] < pivot]
        mid = [arr[i] for i in range(len(arr)) if arr[i]==pivot]
        right = [arr[i] for i in range(len(arr)) if arr[i] > pivot]
        return quick(left) + mid + quick(right)

    print(f"#{test_case} {quick(arr)[N//2]}")
    
        