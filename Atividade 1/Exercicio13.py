#13° Nota do aluno
# Pedir a nota (entre 0 e 10). Se for 7 ou mais, o aluno está aprovado. Se estiver entre 5 e 6,9, o aluno esta em recuperação. Se for menor que 5, esta reprovado. Mostrar o resultado.

print('Validação de nota')
nota = float(input('Digite a nota: '))
if nota >= 7:
    print('O aluno está aprovado!')
elif nota >= 5 and nota <= 6.9:
    print('O aluno está em recuperação!')
else:
    ('O aluno está reprovado!')