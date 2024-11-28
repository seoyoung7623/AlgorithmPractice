# 연속된 부분 수열의 합 Lv2
'''
연속된 부분 수열의 경우 인덱스를 L,R로 나누어 sum 값이 크면 L을 +1, sum 값이 작을경우 R +1하여 부분수열의 값을 
sum에 맞춰 나간다.
'''
def solution(sequence, k):
    L,R = 0,0
    answer = []
    sum = sequence[0]
    while 1:
        
        # for i in range(L,R+1): #시간초과
        #     sum += sequence[i]
        if sum > k:
            sum -= sequence[L]
            L += 1
        elif sum < k:
            R += 1
            if R == len(sequence):
                break
            sum += sequence[R]
        else:
            answer.append([L,R])
            sum -= sequence[L]
            L += 1
    answer.sort(key=lambda x:x[1]-x[0])
    return answer[0]
print(solution([1, 1, 1, 2, 3, 4, 5],5))