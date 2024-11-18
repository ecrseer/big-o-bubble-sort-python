def bubble_sort(lista):
    for atual in range(0, len(lista) - 1):
        for proximo in range(0, len(lista) - atual - 1):
            if lista[proximo] > lista[proximo + 1]:
                lista[proximo], lista[proximo + 1] = lista[proximo + 1], lista[proximo]
    return lista


def questao_2():
    sord = bubble_sort([32, 51, 12, 55, 32, 11, 1])
    print('\nQuestao 2: Comparação entre Complexidade de Tempo e Espaço\n', sord)
