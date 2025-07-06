#Calcular o IMC
#P edir o pesoa (em KG) e altura (em cm). Calcular IMC da pessoa usando a fórmula: peso dividido pela altura ao quadrado. Compara o IMC com a faixa: Menos que 18,5: Abaixo do peso / Entre 18,5 e 24,9: Peso normal / Entre 25 e 29,9: Sobrepeso / 30 ou mais: Obesidade. Mostrar classificação.

print('Calculo de IMC')
peso = float(input('Digite sue peso em KG: '))
altura = float(input('Digite sua altura em centímetros: '))
imc = peso/altura**2

if imc >=30:
    print('Você está com Obesidade!')
elif imc >=25 and imc <= 29.9:
    print ('Voce esta com Sobrepeso!')
elif imc >= 18.5 and imc < 24.9:
    print('Seu peso está normal!')
else:
    print('Você está Abaixo Peso!')