numero = int(input('Digite um número: '))
print('''Escolha uma das bases para a conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
escolha = int(input('Sua opção: '))

if escolha == 1:
    print('{} convertido para binário é = {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} convertido para octal é = {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} convertido para hexadecimal é {}'.format(numero, hex(numero)[2:]))
else:
    print('Escolha inválida. Tente novamente.')
