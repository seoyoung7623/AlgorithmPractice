# 1339 단어숫자 G4
'''
1. 자릿수에따라 숫자가 다르게 지정
2. 그 알파벳의 횟수에 따라 다르게 지정
알파벳의 자릿수와 횟수를 더한다. 가장 큰 수 부터 9~0을 지정해준다.
'''
N = int(input())
alpha = {}
for _ in range(N):
    str = input()
    x = len(str)-1
    for s in str:
        if s not in alpha:
            alpha[s] = 10**x
        else:
            alpha[s] += 10**x
        x -= 1

alpha_list = list(alpha.values())
alpha_list.sort(reverse=True)
ans = 0
num = 9
for i in alpha_list:
    ans += i*num
    num -= 1
print(ans)

