import os
while True:
    num=int(input('ingrese el primer numero: '))
    num2=int(input('ingrese el primer numero: '))
    operacion=input('ingrese la operacion a realizar\n " + , - , * , / " : ')
    os.system('clear')
    if operacion == '+':
        print(f'la suma es {num+num2}')     
    elif operacion == '-':
        print(f'la resta es {num-num2}')
    elif operacion == '*':
        print(f'la multiplicacion es {num*num2}')
    elif operacion == '/':
        print(f'la division es {num/num2}')
    else:
        print(f'la operacion es incorrecta')
    