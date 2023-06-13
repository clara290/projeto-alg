import funcoesusuarios as fu
from funcoesusuarios import *

vendedores = []
produtos = {}
compras = []

while True:
    opcao = exibir_menu()


    if (opcao == 1):

        login, senha = criarloginsenha(vendedores)

        print(login + senha)
        achei = verificarLoginExistente(login, senha)


        nome = verificarnome()
        cpf = verificarcpf(vendedores)
        idade = verificaridade()
        sexo = verifsexo()
        civil = veridcivil()


        vendedores.extend([login, senha, nome, idade, sexo, civil, cpf])

        print('Cadastro feito com sucesso!')

    elif (opcao == 2):
        logado, login = fu.login(vendedores)
        if(logado):
                while True:

                    op2 = fu.outro_menu()
                    if(op2 == 1):
                        vendedores = atualizar_info(vendedores)

                    if(op2 == 2):
                        produtos = cadastrar(produtos)


                    if(op2 == 3):
                        produtos = remover(produtos)

                    if(op2 == 4):
                        busca = buscar_prod(produtos)

                    if(op2 == 5):
                       atualizar = atualizar_prod(produtos)

                    if(op2 == 6):
                        print('obrigado pela preferencia')
                        break
        else:
            print('login ou senha invalidos')

    elif(opcao == 3):

        while True:
            escolha = menu_cliente()

            if (escolha == 1):
                busca = buscar(produtos, compras)

            if(escolha == 2):
                compras = minhas_compras(compras, produtos)

            if (escolha == 3):
                saida = consultarchatgpt(produtos)
                print(saida)

            if(escolha == 4):
                print('obrigado pela preferencia')
                break

    elif(opcao == 4):
        print("Obrigada pela preferência!")
        break



