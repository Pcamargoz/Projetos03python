import random
print('Vamo jogar pedra papel ou tesoura !!')
escolha = str(input('Faça sua escolha:')).lower()
lista = ['pedra', 'tesoura', 'papel']
pc = random.choice(lista)
print('A escolha do computador foi: {}'.format(pc))
if (escolha == 'pedra' and pc == 'tesoura') or (escolha == 'papel' and pc == 'pedra') or (escolha == 'tesoura' and pc == 'papel'):
    Ganhador = 'jogador'
    print('\033[4;34mVocê Ganhou !!!!\033[m')
elif escolha == pc:
    ganhador = 'Empate'
    print('\033[4;32m Houve um empate !!!\033[m')
else:
    ganhador = 'Computador'
    print('\033[4;31mO computador venceu !!!\033[m')