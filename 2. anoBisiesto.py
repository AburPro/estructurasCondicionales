from os import system
system('clear')
year=int(input('ingrese el año a validar'))
if (year < 1582 and year % 4 == 0):
    print(f'el año {year} es bisiesto')
elif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'el año {year} es bisiesto')
else: print(f'el año {year} no es bisiesto')