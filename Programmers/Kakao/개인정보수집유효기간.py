# 개인정보 수집 유효기간

def set_day(date):
    year,month,day = map(int,date.split('.'))
    return year * (28*12) + month * 28 + day

def solution(today, terms, privacies):
    today = set_day(today)
    terms_dic = {key:int(value)*28 for key, value in (item.split(' ') for item in terms)}
    answer = []

    for p in range(len(privacies)):
        date,term = privacies[p].split()
        date = set_day(date)
        if terms_dic[term] + date <= today:
            answer.append(p+1)
    return answer
    # for p in range(len(privacies)):
    #     date,term = privacies[p].split(' ')
    #     year,month,day = map(int,date.split('.'))
    #     month += terms_dic[term]
    #     if  month> 12:
    #         month %= 12
    #         year += 1
    #     day -=1
    #     if day == 0:
    #         month -= 1
    #         day = 28


    #     if year < today[0]:
    #         answer.append(p+1)
    #         continue
    #     if month < today[1]:
    #         answer.append(p+1)
    #         continue
    #     if day < today[2]:
    #         answer.append(p+1)
    #         continue
    # return answer

print(solution("2022.05.19",["A 6", "B 12", "C 3"],["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))