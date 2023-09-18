def solution(quiz):
    answer = []
    for i in quiz:
        i = i.split()
        result = False
        if i[1] == '+':
            if int(i[0]) + int(i[2]) == int(i[4]):
                result = True
        elif i[1] == '-':
            if int(i[0]) - int(i[2]) == int(i[4]):
                result = True
        answer.append("O" if result else "X")
    return answer
