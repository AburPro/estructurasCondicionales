from os import system
system('clear')
palabra1=input('Escriba la palabra 1: ')
palabra2=input('Escriba la palabra 2: ')
p1=len(palabra1)
p2=len(palabra2)
diferencia= p1-p2
if p1 == p2:
    print(f'Las palabras {palabra1} y {palabra2} tienen el mismo largo ')
elif p1>p2:
    print(f'La palabra {palabra1} tiene {diferencia} letras mas que {palabra2}')
else:
    print(f'La palabra {palabra2} tiene {diferencia*-1} letras mas que {palabra1}')