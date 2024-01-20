from os import system
system('clear')
caracter=input('ingrese el caracter: ')

if caracter.isalpha():
    print(f'el caracter {caracter} es una letra')
    if caracter.isalpha()==caracter.isupper():
        print(f'Ademas la letra {caracter} es MAYUSCULA')
    else:
        print(f'Ademas la letra {caracter} es minuscula')
elif caracter.isnumeric():
    print(f'el caracter {caracter} es un numero')
else:
    print(f'el caracter {caracter} no es ni letra ni numero')   
