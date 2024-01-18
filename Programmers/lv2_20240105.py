def solution(e, starts):
    answer = []
    lst = [0] * (e+1)
    for i in range(1,e+1):
        cnt = 0
        for j in range(1,int(i**0.5)+1):
            if j*j == i:
                cnt += 1
            elif i%j == 0:
                cnt += 2
        lst[i] = cnt
    for i in starts:
        answer.append(lst.index(max(lst[i:e+1]),i,e+1))
    return answer
print(solution(8,[1,3,7]))