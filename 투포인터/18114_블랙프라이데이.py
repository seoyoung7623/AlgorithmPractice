# 18114 블래프라이데이 G5
'''
투포인터
38퍼에서 시간초과..
투포인터 + 이분탐색
'''
import sys
input = sys.stdin.readline

N,C = map(int,input().split())
arr = list(map(int,input().split()))

arr.sort()

# 이분 탐색
# 3개 선택 시 남은 하나는 이분 탐색
def binary_serch(left,right,diff):
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == diff:
            return True
        elif arr[mid] > diff:
            right = mid - 1
        else:
            left = mid + 1
    return False

def check(N,C):
    set_arr = set(arr)
    if C in set_arr:
        return True
    i,j = 0,N-1
    while i < j:
        total = arr[i] + arr[j]
        if total > C:
            j -= 1
        elif total == C:
            return True
        else: # 합이 작은 경우 하나를 더 추가
            diff = C - total
            if arr[i] != diff and arr[j] != diff and binary_serch(i,j,diff): #하나를 추가했을때 합이 가능해지면 True 리턴
                return True
            # if diff in set_arr: # 틀린 이유 set은 중복을 제거하기 때문에 불가능!
            #     return True
            i += 1

if check(N,C):
    print(1)
else:
    print(0)
