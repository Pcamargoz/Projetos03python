print('_-'*20)
print('\033[0;31;40mAnalisador de Triângulos\033[m')
print('_-'*20)
a = float(input('\033[0;31;40mDigite aqui o primeiro segmento:\033[m'))
b = float(input('\033[0;31;40mDigite o comprimento do segundo segmento:\033[m'))
c = float(input('\033[0;31;40mDigite o comprimento do terceiro segmento:\033[m'))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima {}PODEM FORMAR{} um triângulo'.format('\033[0;33;40m','\033[m'))
else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo'.format('\033[0;33;40m','\033[m')) 