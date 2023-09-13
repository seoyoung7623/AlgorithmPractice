# 숫자와 문자열과 영단어
# 카카오 채용형 인턴십 Lv1

# def solution(s):
#     english = []
#     answer = []
#     def initial(e):
#         nonlocal english
#         if e == "zero":
#             answer.append('0')
#             english = []
#         elif e == "one":
#             answer.append('1')
#             english = []
#         elif e == "two":
#             answer.append('2')
#             english = []
#         elif e == "three":
#             answer.append('3')
#             english = []
#         elif e == "four":
#             answer.append('4')
#             english = []
#         elif e == "five":
#             answer.append('5')
#             english = []
#         elif e == "six":
#             answer.append('6')
#             english = []
#         elif e == "seven":
#             answer.append('7')
#             english = []
#         elif e == "eight":
#             answer.append('8')
#             english = []
#         elif e == "nine":
#             answer.append('9')
#             english = []

#     for i in s:
#         if i.isalpha():
#             english.append(i)
#             initial(''.join(english))
#         elif i.isdigit():     
#             answer.append(i)
#     return int(''.join(answer))

# 딕셔너리로 깔끔하게 해결하는 방법
num_dic = {
    "zero":'0',
    "one":'1',
    "two":'2',
    "three":'3',
    "four":'4',
    "five":'5',
    "six":'6',
    "seven":'7',
    "eight":'8',
    "nine":'9'
}
def solution(s):
    answer = s
    for key,value in num_dic.items():
        answer = answer.replace(key,value)
    return int(answer)

print(solution("one4seveneight"))