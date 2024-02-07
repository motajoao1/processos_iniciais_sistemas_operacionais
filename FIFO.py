class Fila:
  def __init__(self):
      self.items = []

  def esta_vazia(self):
      return self.items == []

  def adicionar(self, item):
      self.items.append(item)

  def remover(self):
      if not self.esta_vazia():
          return self.items.pop(0)
      else:
          return "A fila está vazia."

  def tamanho(self):
      return len(self.items)

  def frente(self):
      if not self.esta_vazia():
          return self.items[0]
      else:
          return "A fila está vazia."

# Exemplo de uso
fila = Fila()

# Adicionando elementos à fila
fila.adicionar(1)
fila.adicionar(2)
fila.adicionar(3)
fila.adicionar(4)
fila.adicionar(5)
fila.adicionar(6)
fila.adicionar(7)
fila.adicionar(8)
fila.adicionar(9)
fila.adicionar(10)

print("Frente da fila:", fila.frente())  # Mostra o primeiro elemento da fila
print("Tamanho da fila:", fila.tamanho())  # Mostra o tamanho da fila

# Removendo elementos da fila
print("Removido:", fila.remover())  # Remove o primeiro elemento da fila

print("Frente da fila após remoção:", fila.frente())  # Mostra o novo primeiro elemento da fila
print("Tamanho da fila após remoção:", fila.tamanho())  # Mostra o tamanho atualizado da fila
