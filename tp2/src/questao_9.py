def itera_ordenando(lista, index_fim):
    tudo_ordenado = True
    for i in range(index_fim):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            tudo_ordenado = False
    return lista, tudo_ordenado


def ordena_lista_numeros(lista):
    index_fim = len(lista) - 1
    tudo_ordenado = False

    while not tudo_ordenado:
        tudo_ordenado = True
        lista, tudo_ordenado = itera_ordenando(lista, index_fim)
        index_fim -= 1
    return lista


def questao_9():
    print("\nQuestao 9 - Ordenando uma Lista sem Funções Prontas")
    ordenada = ordena_lista_numeros([1, 55, 3, 5, 4])
    print(ordenada)
