import json

def carregar_produtos():
    arquivo = open("produtos.json", "r", encoding="utf-8")
    produtos = json.load(arquivo)
    arquivo.close()
    return produtos

def salvar_produtos(produtos):
    arquivo = open("produtos.json", "w", encoding="utf-8")
    json.dump(produtos, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()

def mostrar_lista(produtos):
    for cada_item in produtos: 
        print(f"ID: {cada_item['id']} | Nome: {cada_item['nome']} | Categoria: {cada_item['categoria']} | Preço: {cada_item['preco']} | Estoque: {cada_item['estoque']}")

def registrar_chegada(produtos):

    busca = int(input("Digite o ID do produto: "))
    quantidade = int(input("Quantas unidades chegaram? "))

    id_encontrado = False

    for cada_item in produtos:
        if cada_item['id'] == busca:
            cada_item['estoque'] += quantidade
            salvar_produtos(produtos)
            print(f"Estoque do produto {busca} atualizado! Novo estoque: {cada_item['estoque']}")
            id_encontrado = True

    if not id_encontrado:
        print("Produto não encontrado! Tente outro ID.")

def registrar_saida(produtos):
    
    busca = int(input("Digite o ID do produto: "))
    quantidade = int(input("Quantas unidades saíram? "))
    
    id_encontrado = False
    
    for cada_item in produtos:
        if cada_item['id'] == busca:
            if quantidade > cada_item['estoque']:
                print(f"Não há produtos suficientes no estoque de {busca}.")
            else:
                cada_item['estoque'] -= quantidade
                salvar_produtos(produtos)
                print(f"Estoque do produto {busca} atualizado! Novo estoque: {cada_item['estoque']}")
                id_encontrado = True

    if not id_encontrado:
        print("Produto não encontrado! Tente outro ID.")

def cadastrar_novo_produto():
    
    opcoes = ["sim", "não", "nao"]
    
    resposta1 = input("Você deseja cadastrar um novo produto? (Sim/Não) ").lower()
    while resposta1 not in opcoes:
        resposta1 = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()
    
    while resposta1 == "sim":

        id_adicao = int(input("Digite um ID para o produto que será adicionado: "))
        
        id_existe = False
        
        for cada_item in produtos:
            if cada_item['id'] == id_adicao:
                id_existe = True

        if id_existe:
            print("Esse ID já existe! Escolha outro ID.")
        else:
            nome_adicao = input("Digite o nome do novo produto: ")
            categoria_adicao = input("Digite a categoria do novo produto: ")
            preco_adicao = float(input("Digite o preço do novo produto: ").replace(",", "."))
            estoque_adicao = int(input("Digite a quantidade em estoque: "))
            
            novo_produto = {
                'id': id_adicao,
                'nome': nome_adicao,
                'categoria': categoria_adicao,
                'preco': preco_adicao,
                'estoque': estoque_adicao
            }
            produtos.append(novo_produto)
            salvar_produtos(produtos)
            print("Novo produto adicionado com sucesso ao Relatório de Controle de Estoque!")
        
        resposta1 = input("Deseja cadastrar outro produto? (Sim/Não) ").lower()
        while resposta1 not in opcoes:
            resposta1 = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()

def editar_produto(produtos):
    
    opcoes = ["sim", "não", "nao"]

    resposta2 = input("Você deseja editar um produto? (Sim/Não) ")
    while resposta2 not in opcoes:
       resposta2 = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()

    while resposta2 == "sim":

        id_edicao = int(input("Digite o ID do produto que será editado: "))

        id_encontrado = False

        for cada_item in produtos:
            if cada_item['id'] == id_edicao:
                nome_edit = input("Edite o nome do produto: ")
                categoria_edit = input("Edite a categoria do produto: ")
                preco_edit = float(input("Edite o preço do produto: ").replace(",", "."))
                print("Obs.: Para editar a situação do estoque, vá nas opções 'Registrar chegada de produtos' ou 'Registrar saída de produtos'.")

                cada_item['nome'] = nome_edit
                cada_item['categoria'] = categoria_edit
                cada_item['preco'] = preco_edit
                salvar_produtos(produtos)
                print(f"Informações do produto {id_edicao} atualizadas com sucesso!")
                id_encontrado = True
        
        if not id_encontrado:
            print("Produto não encontrado! Tente outro ID.")

        resposta2 = input("Deseja cadastrar outro produto? (Sim/Não) ").lower()
        while resposta2 not in opcoes:
            resposta2 = input("Resposta inválida! Responda somente com 'Sim' ou 'Não': ").lower()

produtos = carregar_produtos()

while True:

    print("1 - Mostrar Relatório de Controle de Estoque")
    print("2 - Registrar chegada de produtos")
    print("3 - Registrar saída de produtos")
    print("4 - Cadastrar novo produto")
    print("5 - Editar produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_lista(produtos)
    elif opcao == "2":
        registrar_chegada(produtos)
    elif opcao == "3":
        registrar_saida(produtos)
    elif opcao == "4":
        cadastrar_novo_produto()
    elif opcao == "5":
        editar_produto(produtos)
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida!")
