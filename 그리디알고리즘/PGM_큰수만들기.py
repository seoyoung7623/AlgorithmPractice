# 큰 수 만들기 Lv2 
def solution(number, k):
    answer = ''
    stack = []
    number = list(map(int,number))
    for i in number:
        if len(stack) == 0:
            stack.append(i)
            continue
        while stack and stack[-1] < i and k>0:
            stack.pop()
            k -= 1
        stack.append(i)
    return ''.join(list(map(str,stack[:len(stack) - k])))
print(solution("91999",2))