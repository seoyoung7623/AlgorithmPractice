# 대충 만든 자판
'''
문자열 비교 문제는 딕셔너리를 이용한다.
'''
def solution(keymap, targets):
    answer = []
    
    dic = {}
    
    # 해당 문자열 찾기는 딕셔너리 이용!
    for row in keymap:
        for idx, i in enumerate(row):
            if i not in dic:
                dic[i] = idx+1
            else:
                dic[i] = min(dic[i],idx+1)
    for target in targets:
        flag = False
        sum = 0
        for i in target:
            if i not in dic:
                answer.append(-1)
                flag = True
                break
            else:
                sum += dic[i]
        if flag:
            continue
        else:
            answer.append(sum)
                    
    return answer

print(solution(["AA"],["B","ABA"]))