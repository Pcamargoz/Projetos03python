print('Elevador')
Pessoas = int(input('Quantas pessoas vão para o elevador??:'))
total = int(input('Ao total quantos kilos todos pesam?:'))
if Pessoas >=8:
    print('Atingiu o execesso maximo de pessoas !!')
    print('Reajuste o numero de pessoas para que possam entrar no elevador !!!')
elif total >= 600:
    print('O peso e demais para o elevador !!!')
    print('Reajuste as pessoas para que possam entrar no elevador !!')
else:
    print('Pode entrar no elevador !!')
    print('Tenha uma boa viagem !!!')
