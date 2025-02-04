#1 é pra email repetido
#2 é senha mt curta ou mt longa
#3 dados de senha errada
#4 logado
#5 informaçoes de login errada
#6 excluido
try:
    from controller import ControllerUsuario

    while True:
        x = int(input('digite [1] para cadastrar novo usuario\n'
              'digite [2] para logar na sua conta\n'
              'digite [3] para excluir sua conta\n'
              ))
        if x == 1:
            nome = input('digite seu nome:')
            email = input('digite um email:')
            senha = input('digite uma senha:')
            cadastro = ControllerUsuario.cadastrar_usuario(senha=senha,email=email,nome=nome)
            if cadastro == 1:
                print('email ja cadastrado na plataforma')
            elif cadastro == 2:
                print('Sua Senha é muito longa ou Muito Curta,digite algo entre 8 a 10 caracteres')
            else:
                print('cadastro feito com sucesso')
        elif x == 2:
            email = input('digite um email:')
            senha = input('digite uma senha:')
            logar = ControllerUsuario.logar(senha=senha,email=email)
            if logar == 4:
                print('voce foi logado com sucesso')
            elif logar == 5:
                print('Dados Incorretos.')
        elif x == 3:
            email = input('digite um email:')
            senha = input('digite uma senha:')
            excluir = ControllerUsuario.deletar_usuario(senha=senha,email=email)
            if excluir == 3:
                print('Senha ou Email Incorreto')
            elif excluir == 6:
                print('exluido com sucesso')
            
        else:
            print('escolha uma opção valida')
            continue
except:
    pass
