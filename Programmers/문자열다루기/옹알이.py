# def solution(babbling):
#     answer = 0
#     for i in babbling:
#         word = ""
#         cnt = 0
#         for j in i:
#             word += j
#             if word in ["aya","ye","woo","ma"]:
#                 word = ""
#                 cnt += 1
#         if word == "" and cnt >= 1:
#             answer += 1
#     return answer

# print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))

# 옹알이 2
def solution(babbling):
    answer = 0
    for i in babbling:
        lst = ["aya","ye","woo","ma"]
        word = ""
        back = ''
        cnt = 0
        for j in i:
            word += j
            if word in lst and word != back:
                back = word
                word = ""
                cnt += 1             
        if word == "" and cnt >= 1:
            answer += 1
    return answer

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))