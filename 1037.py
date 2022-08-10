num = int(input("답:"))

for i in range(1,num+1):
    if num % i == 0:
        print(i,end=' ')
print()

##

n = int(input("수:"))
a_list = list(map(int,input().split())) #리스트를 정수형으로 바꿔줌 map
a_max = max(a_list)
a_min = min(a_list)
print(a_max*a_min)
