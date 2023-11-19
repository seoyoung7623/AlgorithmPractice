# 16922 로마숫자만들기 S3
'''
백트랙킹
하지만, 겹치는 숫자가 있을 수 있기때문에 result를 리스트가 아니라 집합을 이용해
겹치는 숫자를 제거해준다.
'''
loma = [1,5,10,50]
n = int(input())
result = set()
def backtrack(start,sum,count):
    for i in range(start,len(loma)):
        if count == n:
            result.add(sum)
            return
        sum += loma[i]
        backtrack(i,sum,count+1)
        sum -= loma[i]

backtrack(0,0,0)
print(len(result))
    
