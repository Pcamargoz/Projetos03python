v = int(input('Digite a velocidadde que seu carro esta'))
multa = v * 7.0
if v >=80:
    print('Voce foi multado e sua multa e de {:.1f}'.format(multa))
else:
    print('Você não foi multado !')