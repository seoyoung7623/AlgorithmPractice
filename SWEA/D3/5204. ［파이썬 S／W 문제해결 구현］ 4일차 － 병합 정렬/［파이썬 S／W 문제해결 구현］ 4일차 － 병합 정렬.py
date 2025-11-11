T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int,input().split()))
    cnt = 0
    
    def merge_sort(arr):        
        def merge(a,b):
            global cnt
            lst = []
            x,y = 0,0
            if a[-1] > b[-1]:
                #print(a,b)
                cnt += 1
                
            while True:
                if x >= len(a):
                    lst.extend(b[y:])
                    break
                if y >= len(b):
                    lst.extend(a[x:])
                    break
                if a[x] <= b[y]:
                    lst.append(a[x])
                    x += 1
                else:
                    lst.append(b[y])
                    y += 1
            return lst

        if len(arr) == 1:
            return arr
        mid = len(arr) // 2
        left = arr[0:mid]
        right = arr[mid:N]
        return merge(merge_sort(left), merge_sort(right))
    print(f"#{test_case} {merge_sort(arr)[N//2]} {cnt} ")