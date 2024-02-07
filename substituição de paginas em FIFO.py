class FIFOPageReplacement:
  def __init__(self, capacity):
      self.capacity = capacity
      self.pages = []  # Lista que simula a memória (armazenamento das páginas)
      self.page_set = set()  # Conjunto para verificar se a página já está na memória

  def page_faults(self, pages):
      page_fault_count = 0  # Contador de falhas de página

      for page in pages:
          if page not in self.page_set:  # Se a página não está na memória
              page_fault_count += 1  # Incrementa a contagem de falhas de página

              if len(self.pages) == self.capacity:  # Se a memória está cheia
                  removed_page = self.pages.pop(0)  # Remove a página mais antiga
                  self.page_set.remove(removed_page)  # Remove a página do conjunto

              self.pages.append(page)  # Adiciona a nova página na memória
              self.page_set.add(page)  # Adiciona a página ao conjunto

      return page_fault_count  # Retorna o número total de falhas de página

# Exemplo de utilização:
capacity = 10  # Capacidade da memória
pages = [1, 3, 0, 3, 5, 6, 3, 4, 5, 4, 7]  # Lista de páginas de exemplo

fifo = FIFOPageReplacement(capacity)
page_faults = fifo.page_faults(pages)
print(f"O número total de falhas de página usando FIFO é: {page_faults}")
