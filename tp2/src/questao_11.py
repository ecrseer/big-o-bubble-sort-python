def questao_11():
    print("\nQuestao 11 Comparando Pilhas e Filas")
    fila = FilaAtendimento(5)
    fila.adicionar_cliente({"nome": "Maria"})
    fila.adicionar_cliente({"nome": "João"})
    fila.adicionar_cliente({"nome": "José"})
    fila.adicionar_cliente({"nome": "Pedro"})
    fila.adicionar_cliente({"nome": "Ana"})

    fila.atender_cliente()
    fila.atender_cliente()
    fila.atender_cliente()


class FilaAtendimento:
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

    def adicionar_cliente(self, cliente):
        if self.is_full():
            print("Erro: A fila de atendimento está cheia")
            return

        self.itens[self.fim] = cliente
        self.fim = self.fim + 1
        self.tamanho_atual += 1
        if self.fim == self.tamanho_max:
            self.fim = 0

    def atender_cliente(self):
        if self.is_empty():
            print("Erro: A fila está vazia")
            return None

        primeiro_fila = self.itens[self.inicio]
        self.itens[self.inicio] = None
        self.inicio = self.inicio + 1
        self.tamanho_atual -= 1

        if self.inicio == self.tamanho_max:
            self.inicio = 0

        print(f"Cliente {primeiro_fila['nome']} atendido")
        return primeiro_fila

    def size(self):
        return self.tamanho_atual
