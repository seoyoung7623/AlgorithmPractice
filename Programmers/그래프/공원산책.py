# 공원산책
'''
문제에 요구사항대로푸는 그래프 구현 문제 
'''
def solution(park, routes):
    answer = []
    x,y = 0,0
    
    N,M = len(park),len(park[0])
    for i in range(N):
        for j in range(M):
            if park[i][j] == 'S':
                x=i
                y=j
                break
    for route in routes:
        xx,yy = x,y
        Flag = False
        if route[0] == 'E':
            for cnt in range(int(route[-1])):
                yy +=1
                if 0> yy or yy>=M or park[x][yy] =='X': # 지나갈수없는 곳이면
                    Flag = True
                    break
        elif route[0] == 'S':
            for cnt in range(int(route[-1])):
                xx +=1
                if 0> xx or xx>=N or park[xx][y] =='X': # 지나갈수없는 곳이면
                    Flag = True
                    break
            
        elif route[0] == 'W':
            for cnt in range(int(route[-1])):
                yy -=1
                if 0> yy or yy>=N or park[x][yy] =='X': # 지나갈수없는 곳이면
                    Flag = True
                    break
          
        elif route[0] == 'N':
            for cnt in range(int(route[-1])):
                xx -=1
                if 0> xx or xx>=N or park[xx][y] =='X': # 지나갈수없는 곳이면
                    Flag = True
                    break
        if not Flag:
            x = xx
            y = yy


    return [x,y]

print(solution(["SOO","OXX","OOO"],["E 2","S 2","W 1"]))