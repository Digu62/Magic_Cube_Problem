
import math, random
from enum import Enum

class face():
  #f = 1 #Fundo
  f = "f1f2f3f4f5f6f7f8f9"
  #a = 2 #Atrás 
  a = "a1a2a3a4a5a6a7a8a9"
  #d = 3 #Direita
  d = "d1d2d3d4d5d6d7d8d9"
  #e = 4 #Esquerca
  e = "e1e2e3e4e5e6e7e8e9"
  #c = 5 #Cima
  c = "c1c2c3c4c5c6c7c8c9"
  #b = 6 #Baixo
  b = "b1b2b3b4b5b6b7b8b9"

  #????
  def index(self):
    return self.value -1

#Exibe o estado inicial do cubo
def display():
  print("              -----------                         ")
  print(f"             |\033[1;37;43m X \033[m|\033[1;37;43m X \033[m|\033[1;37;43m X \033[m|                       ")
  print("              -----------                        ")
  print(f"             |\033[1;37;43m X \033[m|\033[1;37;43m X \033[m|\033[1;37;43m X \033[m|                       ")
  print("              -----------                        ")
  print(f"             |\033[1;37;43m X \033[m|\033[1;37;43m X \033[m|\033[1;37;43m X \033[m|                       ")
  print("------------------------------------------------")
  print(f"|\033[1;37;42m W \033[m|\033[1;37;42m W \033[m|\033[1;37;42m W \033[m|\033[1;37;44m Y \033[m|\033[1;37;44m Y \033[m|\033[1;37;44m Y \033[m|\033[1;37;45m B \033[m|\033[1;37;45m B \033[m|\033[1;37;45m B \033[m|\033[0;37;41m A \033[m|\033[0;37;41m A \033[m|\033[0;37;41m A \033[m|")
  print("------------------------------------------------")
  print(f"|\033[1;37;42m W \033[m|\033[1;37;42m W \033[m|\033[1;37;42m W \033[m|\033[1;37;44m Y \033[m|\033[1;37;44m Y \033[m|\033[1;37;44m Y \033[m|\033[1;37;45m B \033[m|\033[1;37;45m B \033[m|\033[1;37;45m B \033[m|\033[0;37;41m A \033[m|\033[0;37;41m A \033[m|\033[0;37;41m A \033[m|")
  print("------------------------------------------------")
  print(f"|\033[1;37;42m W \033[m|\033[1;37;42m W \033[m|\033[1;37;42m W \033[m|\033[1;37;44m Y \033[m|\033[1;37;44m Y \033[m|\033[1;37;44m Y \033[m|\033[1;37;45m B \033[m|\033[1;37;45m B \033[m|\033[1;37;45m B \033[m|\033[0;37;41m A \033[m|\033[0;37;41m A \033[m|\033[0;37;41m A \033[m|")
  print("------------------------------------------------")
  print(f"             |\033[7;37;40m Z \033[m|\033[7;37;40m Z \033[m|\033[7;37;40m Z \033[m|                        ")
  print("              -----------                         ")
  print(f"             |\033[7;37;40m Z \033[m|\033[7;37;40m Z \033[m|\033[7;37;40m Z \033[m|                        ")
  print("              -----------                         ")
  print(f"             |\033[7;37;40m Z \033[m|\033[7;37;40m Z \033[m|\033[7;37;40m Z \033[m|                        ")
  print("              -----------                         ")

#Recebe o estado atual do cubo e a direção a ser rotacionado
def rotacionar(estado_atual, direcao):
    pass


#Função que define o estado inicial e armazena as faces em um vetor.
def estadoInicial():
    #Cada face é constituida por uma string indicando o estado de cada cubie/peça
    f = "f1f2f3f4f5f6f7f8f9"
    a = "a1a2a3a4a5a6a7a8a9"
    d = "d1d2d3d4d5d6d7d8d9"
    e = "e1e2e3e4e5e6e7e8e9"
    c = "c1c2c3c4c5c6c7c8c9"
    b = "b1b2b3b4b5b6b7b8b9"
    estado_inicial = [f,a,d,e,c,b]

#Recebe o estado atual (um vetor com strings) e realiza o calculo da heuristica
def heuristica(estado_atual)