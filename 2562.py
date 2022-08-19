#최댓값

numlist = []
for i in range(9):
    num = int(input())
    numlist.append(num)
print(max(numlist))
print(numlist.index(max(numlist))+1)
