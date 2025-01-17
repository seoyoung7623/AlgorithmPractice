# 11728 배열합치기 S5
N,M = map(int,input().split())
arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

# answer = arr1 + arr2
# answer.sort()
# print(*answer)

# 투포인트로 풀기
one = 0
two = 0
answer = []

while two < M and one < N:
    if arr1[one] <= arr2[two]:
        answer.append(arr1[one])
        one += 1
    elif arr1[one] > arr2[two]:
        answer.append(arr2[two])
        two += 1

# 남은 원소 처리!!
answer.extend(arr1[one:])
answer.extend(arr2[two:])

print(*answer)