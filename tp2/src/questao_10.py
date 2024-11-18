from src.questao_8 import obtem_fila_testes


def questao_10():
    print("\nQuestao 10 Contando Livros com Números Ímpares")
    livros=obtem_fila_testes()
    print(f"Quantidade de livros com números ímpares: {obter_qtd_livros_impares(livros)}")




def obter_qtd_livros_impares(livros=obtem_fila_testes()):
    impares = 0;

    while not livros.is_empty():
        proximo_fila = livros.dequeue()
        if proximo_fila['id'] % 2 != 0:
            impares += 1

    return impares;

