#7° Verificação de senha
# Definir uma senha correta no programa. Pedir que o usuário digite uma senha. Compare a senha digitada com a correta. Mostrar mensagem de acesso permitido ou negado.

print('Verificador de senha')
senhaCadastrada = input('Cadastre uma senha: ')

senha = input('Digite a Senha Cadastrada: ')

if senha == senhaCadastrada:
    print('Acesso Permitido')
else:
    print('Acesso Negado!')