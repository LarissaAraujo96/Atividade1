#6° Verificador de maioridade
# Pedir a idade da pessoa. Verificar se a idade é maior ou igauls a 18. Mostrar a mensagem dizendo se é maior ou menor de idade

print('Verificador de idade')
idade = int(input('Digite a sua idade para fazermos a verificação: '))
if idade >= 18:
    print('Parabéns voce já maior de idade!')
else:
    print('Você não é maior de idade')