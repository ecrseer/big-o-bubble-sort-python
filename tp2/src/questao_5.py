from questao_4 import obtem_pilha_testes


def questao_5(pilha_de_tarefas=obtem_pilha_testes()):
    print("\nQuestao 5: Comparação entre Complexidade de Tempo e Espaço")
    ultima = pilha_de_tarefas.peek()
    print(f"tarefa no topo {ultima}")
