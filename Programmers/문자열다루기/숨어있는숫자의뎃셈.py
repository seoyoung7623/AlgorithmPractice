# def solution(my_string):
#     # 알파벳이면 공백으로 변환하기
#     for i in my_string:
#         if i.isalpha():
#             my_string = my_string.replace(i,' ')
#     my_string = map(int,my_string.split())
    
#     return sum(my_string)
import re
def solution(my_string):
    my_string = re.findall(r'\d+',my_string)
    my_string = list(map(int,my_string))
    return sum(my_string)
print(solution("aAb1B2cC34oOp"))