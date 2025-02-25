import random
escolha = int(input('Digite um numero:'))
numero = random.randint(0, 5)
if numero ==5:
    print('Parabens voce ganhou')
else:
    print('voce perdeu tente de novo')