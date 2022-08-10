#알파벳 수세는 방법
#딕셔너리는 이용한다. dic = {} / 반복문을 돌린다.

#딕셔너리를 이용하면 문자의 중복 (?)를 처리하기 어려움
#따라서 중복을 막는 list를 이용한다.


str = input().upper()
str_list = list(set(str))
cnt = []


for i in str_list:
    count = str.count(i)
    cnt.append(count)
if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(str_list[cnt.index(max(cnt))])