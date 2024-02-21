# 쿠키 구입
'''
구현: 투포인트
'''
# 1. 내 코드
def solution(cookie):
    answer = 0
    if len(cookie) == 1:
        return answer
    for i in range(len(cookie)-1):
        left_sum = cookie[i]
        right_sum = cookie[i+1]
        left,right = i,i+1
        while True:
            if right+1<len(cookie) and left_sum>=right_sum:
                if left_sum == right_sum:
                    answer = max(answer,right_sum)
                right += 1
                right_sum += cookie[right]
            elif left-1>=0 and left_sum<right_sum:
                left -= 1
                left_sum += cookie[left]
            else:
                break
        
    return answer

# 2. 다른 답안
def solution(cookie):
    answer = 0

    for i in range(len(cookie)-1):
        left, right = i, i+1
        left_sum, right_sum = cookie[i], cookie[i+1]
        
        while True:
            if left_sum == right_sum and left_sum > answer:
                answer = left_sum
            if left > 0 and left_sum <= right_sum:
                left -= 1
                left_sum += cookie[left]
            elif right < len(cookie)-1 and left_sum >= right_sum:
                right += 1
                right_sum += cookie[right]
            else:
                break
    return

# 내 코드 최적화
def solution(cookie):
    answer = 0
    if len(cookie) == 1:
        return answer
    for i in range(len(cookie)-1):
        left_sum = cookie[i]
        right_sum = cookie[i+1]
        left,right = i,i+1
        while True:
            if left_sum == right_sum:
                answer = max(answer,right_sum)     
            if right+1<len(cookie) and left_sum>=right_sum:
                right += 1
                right_sum += cookie[right]
            elif left-1>=0 and left_sum<=right_sum:
                left -= 1
                left_sum += cookie[left]
            else:
                break
    return answer
print(solution([1,1,2,3]))