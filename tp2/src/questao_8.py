from questao_4 import Pilha


def questao_8():
    print("\nQuestao 8: 8 Invertendo a Ordem de uma Fila")
    fila = obtem_fila_testes()
    fila.display()
    print("-----------------------")
    invertida = inverter_fila(fila)
    invertida.display()
    return invertida


def inverter_fila(fila):
    pilha = Pilha(fila.tamanho_max);
    fila_invertida = Fila(fila.tamanho_max)
    while not fila.is_empty():
        pilha.push(fila.dequeue())

    while not pilha.is_empty():
        fila_invertida.enqueue(pilha.pop())

    return fila_invertida


class Fila:
    def __init__(self, tamanho_maximo):
        self.inicio = 0
        self.fim = 0
        self.tamanho_max = tamanho_maximo
        self.tamanho_atual = 0
        self.itens = [None] * tamanho_maximo

    def is_empty(self):
        return self.tamanho_atual == 0

    def is_full(self):
        return self.tamanho_atual == self.tamanho_max

    def enqueue(self, item):
        if self.is_full():
            print("Erro: A fila está cheia")
            return

        self.itens[self.fim] = item
        self.fim = self.fim + 1
        self.tamanho_atual += 1
        if self.fim == self.tamanho_max:
            self.fim = 0

    def dequeue(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None

        primeiro_fila = self.itens[self.inicio]
        self.itens[self.inicio] = None
        self.inicio = self.inicio + 1
        self.tamanho_atual -= 1

        if self.inicio == self.tamanho_max:
            self.inicio = 0

        return primeiro_fila

    def peek(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None
        return self.itens[self.inicio]

    def size(self):
        return self.tamanho_atual

    def display(self):
        if self.is_empty():
            print("A fila está vazia")
        else:
            print("Fila:\n")
            for i in range(self.tamanho_atual):
                index = (self.inicio + i) % self.tamanho_max
                print(self.itens[index], end=" ")
            print()


def obtem_fila_testes():
    teste = Fila(5)

    teste.enqueue({
        'id': 37
    })
    teste.enqueue({
        'id': 1
    })
    teste.enqueue({
        'id': 4
    })
    teste.enqueue({
        'id': 17
    })
    return teste
