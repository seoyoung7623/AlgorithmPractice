#평행사변형을 만들수 없는경우
#3개의 점이 한 직선에 있는 경우 / 기울기 비교 = y변화량/x변화량
def length(x1,y1,x2,y2):
    return ((x2-x1)**2+(y2-y1)**2)**(1/2)


x1,y1,x2,y2,x3,y3 = map(int,input().split())

l1 = length(x1,y1,x2,y2)
l2 = length(x2,y2,x3,y3)
l3 = length(x3,y3,x1,y1)
list_l = [l1,l2,l3]
list_l.sort()

min_l = list_l[0]*2+list_l[1]*2
max_l = list_l[1]*2+list_l[2]*2
if (x2-x1)*(y2-y3)==(x2-x3)*(y2-y1):
    print(-1.0)
else:
    print(max_l - min_l)