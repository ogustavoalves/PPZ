username = input('digite um nome de usuário: ')
password = input('digite uma senha: ')

while password == username:
    print('senha e username devem ser diferentes.')
    username = input('digite um nome de usuário: ')
    password = input('digite uma senha: ')

print('cadastro efetuado.')