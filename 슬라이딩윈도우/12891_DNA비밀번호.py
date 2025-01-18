# 12891 DNA 비밀번호 S2
'''
크기가 고정 되어있기 때문에 슬라이딩 윈도우
ACGT가 각각 개수 이상임을 주의하자
'''
S,P = map(int,input().split())
DNA = input()
ACGT = list(map(int,input().split()))
checking = [0,0,0,0]
table = ['A','C','G','T']

count = 0

for i in range(P):
    checking[table.index(DNA[i])] += 1
for i in range(4):
     if checking[i] < ACGT[i]:
         break
else:
    count += 1
          

for i in range(S-P):
    left = DNA[i]
    checking[table.index(left)] -= 1

    right = DNA[i+P]
    checking[table.index(right)] += 1

    for i in range(4):
     if checking[i] < ACGT[i]:
         break
    else:
        count += 1

print(count)
