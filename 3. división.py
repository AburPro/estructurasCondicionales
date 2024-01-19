from os import system
system('clear')
num1= int(input('ingrese el dividendo: '))
num2= int(input('ingrese el divisor: '))
if num1 % num2 == 0:
    print('La divisione es exacta ')
else:
    print('La division no es exacta ')
cociente=num1/num2
resto=(num1%num2)
print(f'Cociente: {round(cociente)-1}')
print(f'Resto: {resto}')
