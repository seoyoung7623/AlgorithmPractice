#1018 체스판 다시 칠하기
#세로 m 가로 n
#다시 확인 브루트포스 알고리즘
#1. 먼저 N*M만큼의 보드를 받아온다.
#2. 8*8로 잘라야 하기에, 행으로 i-7만큼, 열로 j-7만큼 고정시켜 줘야 한다. 이 방법이 아니고서는 인덱스 에러를 잡을 방법을 모르겠다.
#3. 고정시키고 난 이후는, i,j에서 i+8까지, j+8까지 전부 반복하면서 알맞게 체크무늬로 칠해져 있는지 확인한다.
#4. 흰색이 먼저인 경우와 검은색이 먼저있는 경우를 나누어서, 한번에 종합한 후, min()을 사용하여, 최소값을 알아낸다
m,n = map(int,input().split())
original = []
count = []
for _ in range(m):
    original.append(input())

for a in range(m-7):
    for b in range(n-7):
        index1 = 0
        index2 = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2 ==0:
                    if original[i][j] != 'W':
                        index1 +=1
                    if original[i][j] != 'B':
                        index2 +=1
                else:
                    if original[i][j] != 'B':
                        index1 +=1
                    if original[i][j] != 'W':
                        index2 +=1
        count.append(min(index1,index2))
print(min(count))