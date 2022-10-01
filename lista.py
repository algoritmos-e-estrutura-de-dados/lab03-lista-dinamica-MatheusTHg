from node import Node

class Lista:
  inicio = None

  def __init__(self):
    self.inicio = None

  #adicionar no final da lista
  def adicionar(self, valor, inicio = False):
    if(inicio):
      self.adicionar_no_inicio(valor)
    else:
      self.adicionar_no_fim(valor)

  
  def adicionar_no_inicio(self, valor):
    comeco = Node(valor)
    comeco.proximo = self.inicio
    self.inicio = comeco
  
  def adicionar_no_fim(self, valor):
    if(self.inicio == None):
      self.inicio = Node(valor, None)
    else:
      aux = self.inicio
      while (aux.proximo != None):
        aux = aux.proximo
      aux.proximo = Node(valor, None)

  
  def remover(self, valor):
    if self.inicio.valor == valor:
        self.inicio = self.inicio.proximo
    else:
        anterior = None
        sequencia = self.inicio
        while sequencia and sequencia.valor != valor:
            anterior = sequencia
            sequencia = sequencia.proximo
        if sequencia:
            anterior.proximo = sequencia.proximo
        else:
            anterior.proximo = None
      
  def show(self):
    aux = self.inicio
    print("[", end='')
    while (aux.proximo != None):
      print(f"{aux.valor}", end=', ')
      aux = aux.proximo
    print(f"{aux.valor} ]")
