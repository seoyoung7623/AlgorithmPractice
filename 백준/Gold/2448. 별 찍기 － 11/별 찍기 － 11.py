n = int(input())

def draw_star(n):
    if n == 1:
        return ['*']

    prev = draw_star(n//2)
    stars = []
    
    if n == 3:
        return ['  *  ', ' * * ', '*****']

    for s in prev:
        stars.append(' '*(n//2)+s + ' ' * (n // 2))
    for s in prev:
        stars.append(s+' '+s)
    return stars
print('\n'.join(draw_star(n)))