def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)

    for p1,p2 in zip(phone_book,phone_book[1:]):
        if p2.startswith(p1):
            answer = False
            return answer
    # print(list(zip(phone_book, phone_book[1:])))
    return answer
solution(["6", "12", "6789"])