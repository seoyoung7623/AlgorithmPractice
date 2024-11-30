# 25206 너의 평점은 S5
'''
파이썬 소숫점 4자리까지만 출력하는 방법

'''
subject = {'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0}
sum = 0
cnt = 0
for _ in range(20):
    A,B,C = input().split()
    if C == 'P':
        continue
    sum += float(B)*subject[C]
    cnt += float(B)
print("%.6f"%(sum/cnt))
    