class Node:
  valor = 0
  proximo = None
  ant = None

  def __init__(self, valor = 0, proximo = None, ant = None):
    self.valor = valor
    self.proximo = proximo
    self.ant = ant