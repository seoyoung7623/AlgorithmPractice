# 1439 뒤집디 S5
'''
연속된 수를 하나로 처리한다.
'''
S = input()
num = 1
for i in range(1,len(S)):
    if S[i] != S[i-1]:
        num += 1
print(num//2)
    
        

    