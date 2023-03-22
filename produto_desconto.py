print('Calculadora de desconto de 5%')
prod = float(input('Digite o valor de seu produto: R$'))
desc = prod - (prod * 5 / 100)
print('O valor do produto com desconto aplicado é de R${:.2f}'.format(desc))