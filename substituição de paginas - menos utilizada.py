class LRUPageReplacement:
  def __init__(self, capacity):
      self.capacity = capacity
      self.pages = []  # Lista que simula a memória (armazenamento das páginas)
      self.page_indices = {}  # Dicionário para armazenar índices das páginas
      self.time = 0  # Contador de tempo para controlar o uso das páginas

  def page_faults(self, pages):
      page_fault_count = 0  # Contador de falhas de página

      for page in pages:
          if page not in self.pages:  # Se a página não está na memória
              page_fault_count += 1  # Incrementa a contagem de falhas de página

              if len(self.pages) == self.capacity:  # Se a memória está cheia
                  # Encontra a página menos usada (menor índice de tempo)
                  least_used_page = min(self.page_indices, key=self.page_indices.get)
                  self.pages.remove(least_used_page)  # Remove a página menos usada
                  del self.page_indices[least_used_page]  # Remove do dicionário de índices

              self.pages.append(page)  # Adiciona a nova página na memória
              self.page_indices[page] = self.time  # Atualiza o tempo de uso da página
          else:
              self.page_indices[page] = self.time  # Atualiza o tempo de uso da página existente

          self.time += 1  # Incrementa o contador de tempo

      return page_fault_count  # Retorna o número total de falhas de página

# Exemplo de utilização:
capacity = 10  # Capacidade da memória
pages = [1, 3, 0, 3, 5, 6, 3, 4, 5, 4, 7]  # Lista de páginas de exemplo

lru = LRUPageReplacement(capacity)
page_faults = lru.page_faults(pages)
print(f"O número total de falhas de página usando LRU é: {page_faults}")
