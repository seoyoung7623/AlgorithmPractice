# 10799. 쇠막대기
# 스택, 자료구조

_list = list(input())
stack = []
ans = 0

for i in range(len(_list)):
    if _list[i] == "(":
        stack.append('(')
    else:
        if _list[i-1] == '(':
            stack.pop()
            ans += len(stack)
        else:
            stack.pop() #pop 하면 다음 창이 생겼을때 계산에 오류가 생김!
            ans += 1

print(ans)