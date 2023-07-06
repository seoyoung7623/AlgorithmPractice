'''
다중집합의 개념!
https://velog.io/@munang/%EA%B0%9C%EB%85%90%EC%A0%95%EB%A6%AC-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%8B%A4%EC%A4%91-%EC%A7%91%ED%95%A9
'''

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    str1_set = []
    str2_set = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() & str1[i+1].isalpha():
            str1_set.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() & str2[i+1].isalpha():
            str2_set.append(str2[i:i+2])
    str1_temp = str1_set.copy()
    str1_result = str1_set.copy()
    # 합집합
    for i in str2_set:
        if i not in str1_temp:
            str1_result.append(i)
        else:
            str1_temp.remove(i)
    result = []
    # 교집합
    for i in str2_set:
        if i in str1_set:
            str1_set.remove(i)
            result.append(i)
    if not str1_result:
        answer = 65536
    else:
        answer = int((len(result)/len(str1_result))*65536)
    return answer

print(solution("handshake","shake hands"))