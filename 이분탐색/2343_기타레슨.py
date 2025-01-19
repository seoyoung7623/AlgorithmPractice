# 2342 기타레슨 S1
'''
이분탐색
최소는 가장 긴 강의의 길이(이거보다 작으면 해당강의를 담을 수 없음)
현재 블루레이에 강의를 추가했을때 mid를 초과하면 새로운 블루레이 시작
블루레이개수가 M을 초과하면 해당 크기는 불가능 강의 시간을 늘린다.
'''
# N,M = map(int,input().split())
# arr = list(map(int,input().split()))

# start = max(arr) # 9
# end = sum(arr) # 45
# answer = 0

# while start<=end:
#     count = 1
#     mid = (start + end) // 2
#     sum = 0
#     for i in range(N):
#         if count > M:
#             start = mid+1
#             break
#         sum += arr[i]
#         if sum>mid:
#             count+=1
#             sum = arr[i]            
#     else:
#         if count > M:
#             start = mid + 1
#             continue
#         if sum > mid:
#             start = mid + 1
#         else:
#             end = mid - 1
#             answer = mid
            

# print(answer)

N,M = map(int,input().split())
arr = list(map(int,input().split()))

def divide(max_size,M):
    count = 1
    sum = 0

    for i in range(N):
        if sum + arr[i] > max_size:
            count += 1
            sum = arr[i]
        else:
            sum += arr[i]
    return count <= M

def binary_search(M):
    start = max(arr)
    end = sum(arr)
    answer = end

    while start <= end:
        mid = start + (end-start) // 2
        if divide(mid,M): # count가 작은 경우
            answer = mid
            end = mid - 1
        else: # count가 큰 경우
            start = mid + 1
    return answer

print(binary_search(M))

