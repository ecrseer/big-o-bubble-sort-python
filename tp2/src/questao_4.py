class Pilha:
    def __init__(self, tamanho_maximo=10):
        self.topo = -1
        self.itens = [None] * tamanho_maximo
        self.tamanho_maximo = tamanho_maximo

    def is_full(self):
        return self.topo == self.tamanho_maximo - 1

    def is_empty(self):
        return self.topo == -1

    def push(self, item):
        if self.is_full():
            print("Pilha cheia")
            return
        self.topo += 1
        self.itens[self.topo] = item

    def pop(self):
        if self.is_empty():
            print("Pilha vazia")
            return
        item = self.itens[self.topo]
        self.itens[self.topo] = None
        self.topo -= 1
        return item

    def peek(self):
        if self.is_empty():
            print("Pilha vazia ")
            return
        return self.itens[self.topo]

    def size(self):
        return self.topo + 1

    def display(self):
        if self.is_empty():
            print("Pilha vazia")
        else:
            print("Pilha: ")
            for i in range(self.topo + 1):
                print(self.itens[i])
            print()


def obtem_pilha_testes():
    teste = Pilha(5)
    teste.push({
        "id": 1
    })
    teste.push({
        "id": 4
    })
    teste.push({
        "id": 37
    })
    teste.push({
        "id": 17
    })
    teste.push({
        "id": 12
    })
    return teste

def obtem_pilha_notas():
    teste = Pilha(5)
    teste.push(37)
    teste.push(4)
    teste.push(1)
    teste.push(17)
    teste.push(12)
    return teste


def bubble_sort_ordena_nota(lista, index_fim):
    tudo_ordenado = True
    for i in range(index_fim):
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            tudo_ordenado = False
    return lista, tudo_ordenado


def bubble_sort_completo(lista):
    index_fim = len(lista) - 1
    tudo_ordenado = False

    while not tudo_ordenado:
        tudo_ordenado = True
        lista, tudo_ordenado = bubble_sort_ordena_nota(lista, index_fim)
        index_fim -= 1
    return lista


def questao_4():
    print("Questao 4: Ordenando uma Pilha em Ordem Crescente")
    pilha = obtem_pilha_notas()
    pilha.display()
    print("-------------------")
    a_ordenar = []
    while pilha.is_empty() is False:
        a_ordenar.append(pilha.pop())

    ordenado=bubble_sort_completo(a_ordenar)

    pilha_ordenada = Pilha(len(ordenado))
    for nota in ordenado:
        pilha_ordenada.push(nota)
    pilha_ordenada.display()

