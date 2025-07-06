#8° Per ou Impar
# Pedir um numero ao usuário. Verificar se o numero dividido por 2 tem resto 0. Se tiver é oar senão é impar. Mostrar resultado.

print('Verificador de Par o Impar')
numero = float(input('Digite um numero para a verificação: '))
divisaoNumero = (numero%2)
if divisaoNumero == 0:
    print('Este numero é par')
else:
    print('Esse numero é impar')