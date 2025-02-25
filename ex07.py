salario = float(input('Digite seu salario:'))
n1 = salario + (salario * 15 / 100)
n2 = salario + (salario * 10 / 100)
if salario <= 1250:
    print('Seu salario teve um aumento de 10% sendo assim R${}.'.format(n1))
else:
    print('Seu salario teve um aumento de 15% sendo assim R${}.'.format(n2))