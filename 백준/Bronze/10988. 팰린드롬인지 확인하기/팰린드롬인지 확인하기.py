str = input()
for i in range(len(str)//2+1):
    if len(str) % 2 != 0 and i == len(str)//2:
        continue
    elif str[i] != str[-i-1]:
        print(0)
        break
else:
    print(1)