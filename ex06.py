viagem = int(input('Digite os km de sua viagem:'))
n1 = viagem * 0.50
n2 = viagem * 0.45
if viagem <=200:
    print('O valor de sua viagem e de R${}'.format(float(n1)))
else:
    print('O valor de sua viagem e de R${}'.format(float(n2)))