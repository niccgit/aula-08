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
        print("Produto não encontrado.")

produtos = carregar_produtos()

while True:
    print("1 - Mostrar Relatório de Controle de Estoque")
    print("2 - Registrar chegada de produtos")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        mostrar_lista(produtos)
    elif opcao == "2":
        registrar_chegada(produtos)
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")
