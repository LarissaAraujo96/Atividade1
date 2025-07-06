#3°Divisão inteira e resto.
#  Pedir dois nuemros inteiros ao usuário. Dividir o primeiro número pelo segundo. Mostrar o resultado da divisão inteira (sem casas deciamais). Mostrar o resto da divisão entre os dois nuemros.

print('Resultado inteiro e resto em um divisão')
dividido = int(input('Digite um numero inteiro para ser dividido: '))
dividendo = int(input('Digite um numero inteiro pra ser o dividendo: '))
resultadoInteiro = (dividido//dividendo)
restoDoResultado = (dividido%dividendo)
print(f'O resultado inteiro da divisão é: {resultadoInteiro}')
print(f'O resto da divisão é: {restoDoResultado}')