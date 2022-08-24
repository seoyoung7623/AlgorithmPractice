n = int(input())
for i in range(n):
    strlist = []
    num, str = input().split()

    for j in str:
        print(j*int(num),end='')
    print()


    # for j in range(int(num)):
    #     strlist.append(str)
    # for j in strlist:
    #     print(j,end='')

    
