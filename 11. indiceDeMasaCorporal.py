edad=int(input('escriba su edad: '))
peso=int(input('escriba su peso en kilogramos: '))
estatura=float(input('escriba su estatura en metros: '))
IMC=peso/pow(estatura,2)
while edad<45:
    if IMC>=22:
        print('Riesgo medio')
    else:
        print('Riesgo bajo')
    break
else:
    if IMC>=22:
        print('Riesgo alto')
    else:
        print('Riesgo medio')