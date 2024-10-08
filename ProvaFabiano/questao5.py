def criar_produto(produtos, nomeDoProduto, CodigoDoProduto, PrecoDoProduto, EstoqueDisponivel): 
    produtos.append({
        'nome': nomeDoProduto,
        'codigo': CodigoDoProduto,
        'preco': PrecoDoProduto,
        'estoque': EstoqueDisponivel
    })
    print(f"produto {nomeDoProduto} adicionado com sucesso.")
    return

def atualizar_estoque(produto, quantidade):
    nova_qtd = quantidade
    antiga_qtd = (int(produto['estoque']))
    produto['estoque'] = nova_qtd + antiga_qtd
    print(f"Estoque do produto {produto['nome']} atualizado de {antiga_qtd} para {antiga_qtd + nova_qtd}")
    return

def listar_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
        return
    print("produtos:")
    for produto in produtos:
        print(f"Nome: {produto['nome']}, Código: {produto['codigo']}, Preço: {produto['preco']}, Estoque: {produto['estoque']}")


produtos = []

criar_produto(produtos, "teste1", 1 , 1, 1)
criar_produto(produtos, "teste2", 2 , 2, 2)
criar_produto(produtos, "teste3", 3 , 3, 3)
criar_produto(produtos, "teste4", 4 , 4, 4)

print("-------------------------------------------------------------------------------")
listar_produtos(produtos)
print("-------------------------------------------------------------------------------")

atualizar_estoque(produtos[0], 3)
atualizar_estoque(produtos[1], 5)

print("-------------------------------------------------------------------------------")
listar_produtos(produtos)
print("-------------------------------------------------------------------------------")



