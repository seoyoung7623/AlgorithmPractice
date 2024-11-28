def solution(s):
    answer = True
    lst = []
    for i in range(len(s)):
        if not lst:
            lst.append(s[i])
        else:
            lst.append(s[i])
            if lst[-1] ==")":
                if lst[-2] == "(":
                    lst.pop()
                    lst.pop()
    if lst:
        return False
    return True
