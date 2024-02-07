def sjf(processos):
  tempo_total = 0
  tempo_espera = [0] * len(processos)
  tempo_turnaround = [0] * len(processos)
  processos_ordenados = sorted(processos, key=lambda x: x[1])  # Ordena os processos pelo tempo de chegada

  tempo_total = processos_ordenados[0][1]  # Tempo total começa com o tempo de chegada do primeiro processo
  for i in range(1, len(processos_ordenados)):
      tempo_espera[i] = tempo_total - processos_ordenados[i][1]  # Calcula o tempo de espera
      tempo_total += processos_ordenados[i][2]  # Adiciona o tempo de execução ao tempo total
      tempo_turnaround[i] = tempo_total - processos_ordenados[i][1]  # Calcula o tempo de turnaround

  print("Processo\tTempo de Chegada\tTempo de Execução\tTempo de Espera\tTempo de Turnaround")
  for i in range(len(processos_ordenados)):
      print(f"{processos_ordenados[i][0]}\t\t{processos_ordenados[i][1]}\t\t\t{processos_ordenados[i][2]}\t\t\t{tempo_espera[i]}\t\t\t{tempo_turnaround[i]}")

# Exemplo de uso
if __name__ == "__main__":
  # Lista de processos na forma (nome, tempo_de_chegada, tempo_de_execução)
  processos = [
      ("P1", 0, 6),
      ("P2", 1, 4),
      ("P3", 2, 8),
      ("P4", 3, 3),
      ("P5", 4, 7),
      ("P6", 5, 5),
      ("P7", 6, 3),
      ("P8", 7, 0),
      ("P9", 8, 9),
      ("P10", 8, 8),
  ]

  sjf(processos)
