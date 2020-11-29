casa = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos * 12)
mínimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos, prestação))
print('A prestação será de R${:.2f}'.format(prestação))
if prestação <= mínimo:
    print('Empréstimo \033[32mpode\033[m ser concedido!')
else:
    print('Empréstimo \033[31mnão pode\033[m ser concedido!')
