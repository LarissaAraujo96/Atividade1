#12° Pode dirigir
#Pedir a idade da pessoa. Perguntar se ela possui CNH (responder sim ou não).Verificar se ela tem 18 anos ou mais e se respondeu "sim" para CNH. Mostrar se ela pode dirigir ou não.
print('Permissão para dirigir')
idade = int(input('Digite a sua idade: '))
cnh = input('Você possui CNH sim ou não? ')
if idade >=18 and cnh == 'sim':
    print('Parabéns você pode dirigir!')
else:
    print('Você não pode dirigir!')