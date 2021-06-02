usuarios = []

logado = False

while not logado:
    comando = input('Bem-Vindo! Digite 1 para login ou  2 para criar um novo usuário ou 3 para sair:  ')
    if comando == '1':
        usuario = input('Digite o nome do seu usuário:   ')
        senha = input('Digite a senha para seu usuário:  ')
        for u in usuarios:
            if u ['usuario'] == usuario and u['senha'] == senha:
                logado = True
        if logado == False:
            print('Usuário ou senha invalido')
    elif comando == "2":
        usuario = input('Digite o nome para seu novo usuário:   ')
        senha = input('Digite uma senha para seu usuário:  ')
        usuarios.append({"usuario" : usuario, "senha" : senha})
        print (f"Usuário {usuario} cadastrado com sucesso!")
    elif comando == 'x':
        print('Até logo!!')
        exit(0)
    else:
        print ("Voçê esta de bricandeira?")
noProg = True

while noProg:
    print("Bem vindo ao sistema")
    sair = input('Digite x para sair:  ')
    if sair == 'x':
        exit(0)

# print("Bem-vindo ao Sistema!!!")        