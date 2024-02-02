def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    count = [0,0,0]   
    
    for i in range(len(answers)):
        if s1[i%5] == answers[i]:
            count[0] += 1
        if s2[i%8] == answers[i]:
            count[1] += 1
        if s3[i%10] == answers[i]:
            count[2] += 1
    
    total=max(count)
    for i in range(3):
        if total == count[i]:
            answer.append(i)
    return answer
print(solution([1,2,3,4,5]))