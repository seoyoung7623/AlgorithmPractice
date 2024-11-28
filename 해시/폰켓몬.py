def solution(nums):
    answer = 0
    dic = {}
    n_max = len(nums)//2
    for i in nums:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    if len(list(dic.keys())) >= n_max:
        answer = n_max
    else:
        answer = len(list(dic.keys()))
    return answer
print(solution([3,1,2,3]))