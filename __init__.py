import openai
def verificarLoginExistente(login, vends):
    achei = False
    for i in vends:
        if login == vends[0]:
            achei = True
    return achei

def exibir_menu():
    print('\n-------------BEM VINDO!--------------')
    print('1-Cadastrar vendedor')
    print('2-Fazer login')
    print('3-Acessar menu do cliente')
    print('4-Sair')
    op = int(input('O que voce deseja fazer?: '))
    return op

def outro_menu():
    print('\n------------MENU--------------')
    print('1-atualizar senha/informaçoes pessoais')
    print('2-Cadastrar produto')
    print('3-Remover produto')
    print('4-Buscar produto')
    print('5-Atualizar produto')
    print("6-Deslogar")
    opc = int(input('O que voce deseja fazer?: '))
    return opc

def atualizar_info(vendedores):
    atualizar = input('O que voce deseja atualizar?')
    if (atualizar == 'login'):
        novo_login = input('digite seu novo login:')
        vendedores[0] = novo_login
        if(vendedores[0] == novo_login):
            print('login atualizado!')
        else:
            print("Algo deu errado, por favor, tente novamente")
    elif (atualizar == 'senha'):
        vendedores[1] = input('digite sua nova senha:')
        print('senha atualizada!')

    elif (atualizar == 'idade'):
        vendedores[3] = input('digite sua idade atual:')
        print('idade atualizada!')

    elif (atualizar == 'estado civil'):
        vendedores[4] = input('digite seu novo estado civil:')
        print('estado civil atualizado!')
    else:
        print("Algo deu errado, por favor, tente novamente")
    return vendedores

def cadastrar(produtos):
    produto = input('digite o produto a ser cadastrado: ')
    while produto.isdigit():
        produto = input('Erro. Esse campo só aceita letras. Digite o produto novamente: ')

    for i in produtos:
        if (i == produto):
            print('produto ja cadastrado')

    preco = float(input('digite o preço do produto'))
    quantidade = int(input('digite a quantidade do produto em estoque: '))
    id = input('digite o id do produto')
    produtos[produto] = {'preco': preco, 'quantidade': quantidade, 'id': id}
    print('produto cadastrado com sucesso!')
    return produtos

def remover(produtos):
    remov = input('qual produto deseja remover? ')
    valor_removido = produtos.pop(remov)
    if valor_removido:
        print('produto removido com sucesso!')
    else:
        print('produto nao encontrado!')
    return produtos

def buscar_prod(produtos):
    busca = input('qual produto deseja buscar?')
    valor = produtos.get(busca)

    if valor:
        print('\n--------Produto encontrado----------')
        if busca in produtos:
            print(f'produto: {busca}')
            print(f'preço: {produtos[busca]["preco"]}')
            print(f'quantidade: {produtos[busca]["quantidade"]}')
            print(f'id: {produtos[busca]["id"]}')
            print('-------------------------------------')
    else:
        print('produto nao encontrado')
    return busca

def busca_gpt( produtos):
    busca = input('deseja ver a descriçao de qual produto?')
    valor = produtos.get(busca)
    if valor:
        print(busca)
    return busca
def atualizar_prod(produtos):
    print('---------produtos cadastrados:----------')
    for nome_produto, valores in produtos.items():
        print(f'produto: {nome_produto}')
        print(f'preço: {valores["preco"]}')
        print(f'quantidade: {valores["quantidade"]}')
        print(f'id: {valores["id"]}')
        print('------------------------------------')
    atualizar = input('qual produto voce deseja atualizar? ')
    if atualizar in produtos:
        preco = float(input('digite o novo preço do produto'))
        quantidade = int(input('digite a nova quantidade em estoque:'))
        produtos[atualizar]['preco'] = preco
        produtos[atualizar]['quantidade'] = quantidade

        print('----------produto atualizado-----------')
        if atualizar in produtos:
            print(f'produto: {atualizar}')
            print(f'preço: {produtos[atualizar]["preco"]}')
            print(f'quantidade: {produtos[atualizar]["quantidade"]}')
            print(f'id: {produtos[atualizar]["id"]}')
            print('-------------------------------------')


    else:
        print('produto nao encontrado')
    return atualizar

def criarloginsenha(vendedores):
    login = input('Crie seu login: ')
    while True:
        if verificarLoginExistente(login, vendedores):
            print('esse login ja existe')
            login = input('Crie seu login novamente: ')
        else:
            break

    senha = input('Crie sua senha: ')

    while login == senha:
        print('Error: a senha não pode ser igual ao login!')
        senha = input('crie sua senha novamente: ')

    return [login, senha]

def verificarnome():
    nome = input('digite seu nome completo: ')
    while nome.isdigit():
        nome = input('Error, digite seu nome completo: ')
    return nome


def verificarcpf(vendedores):

    cpf = input('digite seu cpf: ')
    while len(cpf) < 11:
        cpf = input('Error, digite seu cpf: ')
    while cpf.isalpha():
        cpf = input('Error, digite seu cpf: ')

    while True:
        for i in vendedores:
            if i == cpf:
                cpf = input('Esse cpf ja foi cadastrado. Digite novamente: ')
        break
    return cpf

def verificaridade():
    idade = int(input('digite sua idade: '))
    while idade < 18 or idade >= 100:
        idade = int(input('Error, digite sua idade: '))

    return idade

def verifsexo():
    sexo = input('digite seu sexo (f/m): ')
    while (sexo != "f" and sexo != "m"):
        sexo = input('Error, digite seu sexo (f/m): ')
    return sexo

def veridcivil():
    civil = input('digite seu estado civil (s/c/v/d): ')
    while (civil != 's' and civil != 'c' and civil != 'v' and civil != 'd'):
        civil = input('Error, digite seu estado civil (s/c/v/d): ')
    return civil

def login(vendedores):
    login = input('digite seu login: ')
    senha = input('digite sua senha: ')

    for dados in vendedores:
        if vendedores[0] == login and vendedores[1] == senha:
            print('login feito com sucesso. Bem vindo!')
            return [True, login]
    return [False, login]

def menu_cliente ():
    print('\n-----------BEM VINDO CLIENTE!------------')
    print('1- Buscar/comprar produto')
    print('2- Minhas compras')
    print('3- Consultar descrição do produto')
    print('4- Sair')
    escolha = int(input('O que voce deseja fazer? '))
    return escolha

def buscar(produtos, compras):
    compra = 0
    busca = input('digite o nome do produto: ')
    valor = produtos.get(busca)
    if valor:
        print('\n--------informaçoes do produto---------')
        if busca in produtos:
            print(f'produto: {busca}')
            print(f'preço: {produtos[busca]["preco"]}')
            print(f'quantidade: {produtos[busca]["quantidade"]}')
            print(f'id: {produtos[busca]["id"]}')
            print('-------------------------------------')

        print('voce deseja comprar esse produto?')
        resp = input('digite (sim/não): ')
        while resp != 'sim' and resp != 'não':
            resp = input('error, digite (sim/não): ')


        if (resp == 'sim'):
            qtde = int(input('Quantas unidades voce deseja comprar? '))
            if qtde <= produtos[busca]['quantidade']:
                print('compra feita com sucesso! ')
                compra += 1
            else:
                print('quantidade solicitada excede a quantidade em estoque.')
            compras.append(busca)
        else:
            print('ok')
    else:
        print('produto nao encontrado')
    return busca

def minhas_compras(compras, produtos,):
    print('\n---------compras feitas----------')
    for nome_produto, valores in produtos.items():
        print(f'produto: {nome_produto}')
        print(f'preço: {valores["preco"]}')
        print(f'quantidade: {valores["quantidade"]}')
        print(f'id: {valores["id"]}')
        print('------------------------------------')
    return compras

def consultarchatgpt(produtos):
    openai.api_key = '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'
    produto = busca_gpt(produtos)
    model_engine = "text-davinci-003"
    prompt = 'me diga resumidamente o que você acha do ' + produto + ' ?'
    max_tokens = 1024
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=max_tokens,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return  completion.choices[0].text


