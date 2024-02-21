'''
그리디 펠린드롬 수 구하기
완전탐색
'''
def palindrome(lst):
    if lst == lst[::-1]:
        return len(lst)
    else:
        return 0
    

def solution(s):
    answer = 0
    for i in range(len(s)-1):
        for j in range(i+1,len(s)+1):
            answer = max(answer,palindrome(s[i:j]))
    return answer
print(solution("abcdcba"))