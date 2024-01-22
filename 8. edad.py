from time import localtime
t = localtime()
print('escriba su fecha de naciomiento.')
dia=int(input('dia: '))
mes=int(input('mes: '))
año=int(input('año: '))
edad=t.tm_year-año
if t.tm_mday>dia and t.tm_mon>mes:
    print(f'Usted tiene {edad}')
else:
    print(f'Usted tiene {edad-1}')
