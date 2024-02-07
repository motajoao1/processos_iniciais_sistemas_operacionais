import heapq

class Processo:
    def __init__(self, id_processo, tempo_chegada, tempo_execucao, deadline):
        self.id_processo = id_processo
        self.tempo_chegada = tempo_chegada
        self.tempo_execucao = tempo_execucao
        self.deadline = deadline

    def __lt__(self, other):
        # Comparação para heapq (usado na fila de prioridade)
        return self.deadline < other.deadline

class EscalonadorEDF:
    def __init__(self):
        self.processos = []

    def adicionar_processo(self, processo):
        heapq.heappush(self.processos, processo)

    def executar(self):
        tempo_atual = 0

        while self.processos:
            processo = heapq.heappop(self.processos)
            print(f"Executando processo {processo.id_processo} de {processo.tempo_execucao} unidades de tempo.")
            tempo_atual += processo.tempo_execucao

        print("Todos os processos foram executados.")


# Exemplo de utilização:
escalonador = EscalonadorEDF()

# Adiciona os processos (ID, Tempo de Chegada, Tempo de Execução, Deadline)
escalonador.adicionar_processo(Processo(1, 0, 5, 10))
escalonador.adicionar_processo(Processo(2, 2, 3, 8))
escalonador.adicionar_processo(Processo(3, 4, 4, 15))
escalonador.adicionar_processo(Processo(4, 6, 2, 12))
escalonador.adicionar_processo(Processo(5, 0, 5, 10))
escalonador.adicionar_processo(Processo(6, 2, 3, 8))
escalonador.adicionar_processo(Processo(7, 4, 4, 15))
escalonador.adicionar_processo(Processo(8, 6, 2, 12))
escalonador.adicionar_processo(Processo(9, 0, 5, 10))
escalonador.adicionar_processo(Processo(10, 2, 3, 8))

# Executa os processos com o escalonador EDF
escalonador.executar()
