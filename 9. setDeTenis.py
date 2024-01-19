from os import system
system('clear')
m=int(input(f'juegos ganados por A: '))
n=int(input(f'juegos ganados por b: '))
if (n-m) > 3 or (m-n) > 3:
    print('Invalido')
elif n+2<=m and n>=4:
    print(f'Gano el jugador A')
elif m+2<=n and m>=4:
    print(f'Gano el jugador B')
else:
    print('aun no termina')
