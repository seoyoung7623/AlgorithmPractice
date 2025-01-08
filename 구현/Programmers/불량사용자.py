# PGM 불량사용자 
'''
https://school.programmers.co.kr/learn/courses/30/lessons/64064
문자열이 8개 뿐이기 때문에 순열로 모든 경우를 구한다.
여기서 정답 배열중에 중복되는 경우가 있기때문에 중복을 제거한다.
'''
from itertools import permutations

def solution(user_id, banned_id):
    answer = []
    for members in list(permutations(user_id,len(banned_id),)):
        flag = False
        for i in range(len(members)):
            if len(members[i]) == len(banned_id[i]):
                for j in range(len(members[i])):
                    if banned_id[i][j] == '*':
                        continue
                    if members[i][j] != banned_id[i][j]:
                        flag = True
                        break
            else:
                flag = True
            if flag:
                break
        if not flag:
            members = sorted(members)
            if members not in answer:
                answer.append(members)
    return len(answer)

print(solution(	["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]))