class Disco:
  def __init__(self, tamanho):
      self.tamanho = tamanho  # Tamanho total do disco em blocos
      self.dados = [None] * tamanho  # Lista para simular os blocos do disco

  def escrever_bloco(self, numero_bloco, dados):
      if 0 <= numero_bloco < self.tamanho:
          self.dados[numero_bloco] = dados
          print(f"Escrita bem-sucedida no bloco {numero_bloco}.")
      else:
          print("Erro: número de bloco inválido.")

  def ler_bloco(self, numero_bloco):
      if 0 <= numero_bloco < self.tamanho:
          dados = self.dados[numero_bloco]
          if dados is not None:
              print(f"Conteúdo do bloco {numero_bloco}: {dados}")
          else:
              print(f"O bloco {numero_bloco} está vazio.")
      else:
          print("Erro: número de bloco inválido.")


# Exemplo de utilização:
disco = Disco(tamanho=4000)  # Cria um disco de tamanho 4000 blocos

# Escreve no bloco 5
disco.escrever_bloco(5, "Dados do bloco 5")

# Lê o bloco 5
disco.ler_bloco(5)

# Tenta escrever em um bloco inválido
disco.escrever_bloco(150, "Tentativa de escrita em bloco inválido")

# Tenta ler um bloco inválido
disco.ler_bloco(150)
