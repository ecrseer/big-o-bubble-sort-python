from questao_4 import obtem_pilha_testes


def obter_qtd_pedidos_pares(pedidos=obtem_pilha_testes()):
    pares = 0
    for i in range(pedidos.size()):
        if pedidos.itens[i]['id'] % 2 == 0:
            pares += 1

    return pares


def questao_7():
    print("\nQuestao 7: Contando Pedidos Pares na Pilha")
    pedidos = obtem_pilha_testes()
    pedidos.display()
    print("\n-------------------\n")
    impar=obter_qtd_pedidos_pares(pedidos)
    print(f"Quantidade de pedidos pares: {impar}")
