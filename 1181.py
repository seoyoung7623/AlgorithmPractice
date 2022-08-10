list = []
num = int(input())

for _ in range(num):
    word = input()
    if [word,len(word)] not in list:
        list.append([word,len(word)])
list.sort(key = lambda x: x[0])
list.sort(key = lambda x: x[1])

for j in list:
    print(j[0])