#4153 직각삼각형    
while 1:
    numlist = list(map(int,input().split()))
    numlist.sort();
    
    if (numlist[0]==0 & numlist[1]==0 & numlist[2]==0):
        break
    if (((numlist[0]**2 + numlist[1]**2)**0.5) == numlist[2]):
        print("right")
    else:
        print("wrong")

