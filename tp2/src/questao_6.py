from questao_4 import obtem_pilha_testes


def obter_qtd_pedidos_impares(pedidos=obtem_pilha_testes()):
    impares = 0
    for i in range(pedidos.size()):
        if pedidos.itens[i]['id'] % 2 != 0:
            impares += 1

    return impares


def questao_6():
    print("\nQuestao 6:  Contando Pedidos Impares na Pilha")
    pedidos = obtem_pilha_testes()
    pedidos.display()
    print("\n-------------------\n")
    impar=obter_qtd_pedidos_impares(pedidos)
    print(f"Quantidade de pedidos impares: {impar}")
