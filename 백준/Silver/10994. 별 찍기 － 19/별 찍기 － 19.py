N = int(input())

def draw_star(n,canvars):
    length = n*4-3
    for x in range(1,length//2):
        if x % 2 == 0:
            canvars[x] = canvars[x-1].copy()
            for y in range(x,length-x):
                canvars[x][y] = '*'
        if x % 2 == 1:
            for y in range(0,x,2):
                canvars[x][length-y-1] = '*'
                canvars[x][y] = '*'
    for y in range(0,length,2):
        canvars[length//2][y] = '*'
    for x in range(length//2,length):
        canvars[x] = canvars[length-x-1].copy()
    canvars[0],canvars[-1] = ['*']*length,['*']*length

length = N*4-3
canvars = [[' ' for _ in range(length)] for _ in range(length)]
draw_star(N,canvars)

for row in canvars:
    print(''.join(row).rstrip())