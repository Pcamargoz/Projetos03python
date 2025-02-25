a = int(input('Digite um numero:'))
b = int(input('Digite um numero:'))
c = int(input('Digite um numero:'))
# Verificando quem e o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#verificando maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior numero e {}{}{}'.format('\033[1;31;40m',maior,'\033[m'))
print('O menor numero e {}{}{}'.format('\033[1;32;40m',menor,'\033[m'))