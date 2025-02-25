nome = input('\033[0;32;41mDigite seu nome aqui:\033[m')
idade = int(input('\033[0;32;40mAgora sua idade:\033[m'))
print('Prazer em te conhecer {}{}{}, Você tem {}{}{} ANOS ????? que legal'.format('\033[0;32;41m',nome,'\033[m','\033[0;32;41m',idade,'\033[m'))
if idade <= 20:
    print('Você tem {}{}{} Caramba em você esta novo !!!'.format('\033[0;32;41m',idade,'\033[m'))
else:
    print('Você tem {}{}{} Caramba você ja esta velinho em !!!'.format('\033[0;32;40m',idade,'\033[m'))