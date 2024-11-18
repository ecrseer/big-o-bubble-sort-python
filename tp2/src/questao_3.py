def tem_valor_duplicado_o_quadrado(lista):
    for i in range(len(lista)):
        for j in range(len(lista)):
            if i != j and lista[i] == lista[j]:
                return True
    return False


def tem_valor_duplicado_o_linear(numeros):
    numeros_como_index = {
        f"{numeros[0]}": None
    }
    for i in range(len(numeros)):
        if numeros[i] in numeros_como_index:
            return True
        numeros_como_index[numeros[i]] = numeros[i]
    return False


def questao_3():
    print('\nQuestao 3: Priorizar Tempo ou Espaço?\n')
    bruta = tem_valor_duplicado_o_quadrado([31, 55, 12, 55, 32, 11, 1])
    print('\n abordagem bruta:\n', bruta)

    melhorada = tem_valor_duplicado_o_linear([31, 55, 12, 55, 32, 11, 1])
    print('\n melhorada: \n', melhorada)

