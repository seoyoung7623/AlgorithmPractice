#11047 동전0
n,money = map(int,input().split())
coinpak = []
cnt = 0
for i in range(n):
    coin = int(input())
    coinpak.append(coin)
coinpak.sort(reverse=True)
for i in range(len(coinpak)):
    if money>=coinpak[i]:
        cnt += money//coinpak[i]
        money = money%coinpak[i]
print(cnt)
