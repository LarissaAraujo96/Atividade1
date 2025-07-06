#9° Entrada no evento
# Pedir a idade da pessoa. Verificar se está entre 16 e 65 anos(inclusive). Mostrar se a etrada é permitida ou negada.

print('Veriicação de entrada no evento')
idade = int(input('Digite a sua idade: '))
if idade >= 16 and idade <65:
    print('Entrada permitida')
else:
    print('Acesso negado')