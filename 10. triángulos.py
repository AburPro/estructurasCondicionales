a=float(input('ingrese a: '))
b=float(input('ingrese b: '))
c=float(input('ingrese c: '))
while a+b>c and b+c>a and c+a>b:
    if a==b==c:
        print('el triagulo es equilatero')
        break
    elif a==b or a==c or b==c:
        print('el triangulo es isósceles')
        break
    elif a != b != c:
        print('el triangulo es escaleno')
        break
else:
    print('no es un triangulo valido')