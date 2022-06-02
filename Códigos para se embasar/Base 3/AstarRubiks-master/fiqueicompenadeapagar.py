'''
----- Estrutura base -----
- Estados
- Ações
- Heurística
- Fronteira
- Objetivo
- Caminho
- Main
'''

'''
----- Notações -----
- Faces: (6)
Face Direita - 'D'
Face Esquerda - 'E'
Frente - 'F'
Atrás - 'A'
Face de baixo - 'B'
Face de cima - 'C'

- Angulo do movimento(3):
Girando 90º
Girando 180º
Girando 270º || -90º

- Sentidos (2) #Dispensável utilizando o conceito de graus
Horario - 'HO'
Anti-horário 'AH'

- Ações (12)
Girar Direita Horário - 'GDHO'
Girar Direita Anti-horário - 'GDAH'

Girar Esquerda Horário - 'GEHO'
Girar Esquerda Anti-horário - 'GEAH'

Girar Frente Horário - 'GFHO'
Girar Frente Anti-horário - 'GFAH'

Girar Atrás Horário - 'GAHO'
Girar Atrás Anti-horário - 'GAAH'

Girar Baixo Horário - 'GBHO'
Girar Baixo Anti-horário - 'GBAH'

Girar Cima Horário - 'GCHO'
Girar Cima Anti-horário - 'GCAH'

Ordem númerica das faces
Ex: Face da frente
F1 - F2 - F3
F4 - F5 - F6
F7 - F8 - F9
'''

'''
Segunda possibilidade de Ações
- Ações
Girar face no eixo X - x_girar("face","direcao")
Girar face no eixo Y - y_girar("face","direcao")
Girar face no eixo Z - z_girar("face","direcao")
'''

class cuboMagico():
  def __init__(self):
    pass

  def girar_x(face, direcao):
    
    #Verificar se a face pode girar no eixo X (¬(frente || fundo))
    if face not in {"frente", "fundo"}:
      return print(f"A {face} nao pode ser girada no eixo x")

    #Verificar se a direção faz parte do eixo x ("direita" || "esquerda")
    if direcao not in {"direita", "esquerda"}:
      return print(f"A {face} nao pode ser girada na direcao {direcao}")
  
#Incompleto-------------------------------
    

def buscaAEstrela("raiz"):
  #1º Instância um noCorrente (determinará em que ponto está a busca)
  #2º Criar a lista fronteira (lista que armazena todos os nós fronteiras que já foram aberto)
  #3º Variável que indique se o objetivo foi alcançado ou n
  #4º Variavel que indique a quantidade de nós que ainda estão abertos. (talvez baste verificar o tamanho da lista fronteira) 
  #5º Looping para aprofundar na arvore (o looping encerra ao exvaziar a lista fronteira ou alcançar o objetivo)
  #5.1º Função para selecionar o melhor nó a ser aprofundado. (provavelmente se basenado no calculo da heuristica e usando a lista fronteira)
  #5.2º Função para gerar o(os) sucessor(es) e aprofundar(vai aprofundar no nó escolhido)


def selecionaNo(): #Função necessária para a "buscaAEstrela()"

def acoes(acao):
  switch(acao):
    case "GDHO":
        print("Girar Direita Horário")
    case "GDAH":
        print("Girar Direita Anti-Horário")
    case "GEHO":
        print("Girar Esquerda Horário")
    case "GEAH":
        print("Girar Esquerda Anti-Horário")
    case "GFHO":
        print("Girar Frente Horário")
    case "GFAH":
        print("Girar Frente Anti-Horário")
    case "GAHO":
        print("Girar Atrás Horário")
    case "GAAH":
        print("Girar Atrás Anti-Horário")
    case "GBHO":
        print("Girar Baixo Horário")
    case "GBAH":
        print("Girar Baixo Anti-Horário")
    case "GCHO":
        print("Girar Cima Horário")
    case "GCAH":
        print("Girar Cima Anti-Horário")
    default:
      print("Acao invalida)

def display(estado_atual):
  print(f"               |\033[1;37;43m {estado_atual[4][0]+estado_atual[4][1]} \033[m|\033[1;37;43m {estado_atual[4][2]+estado_atual[4][3]} \033[m|\033[1;37;43m {estado_atual[4][4]+estado_atual[4][5]} \033[m|                       ")
  print(f"               |\033[1;37;43m {estado_atual[4][6]+estado_atual[4][7]} \033[m|\033[1;37;43m {estado_atual[4][8]+estado_atual[4][9]} \033[m|\033[1;37;43m {estado_atual[4][10]+estado_atual[4][11]} \033[m|                       ")
  print(f"               |\033[1;37;43m {estado_atual[4][12]+estado_atual[4][13]} \033[m|\033[1;37;43m {estado_atual[4][14]+estado_atual[4][15]} \033[m|\033[1;37;43m {estado_atual[4][16]+estado_atual[4][17]} \033[m|                       ")
  print(f"|\033[1;37;42m {estado_atual[3][0]+estado_atual[3][1]} \033[m|\033[1;37;42m {estado_atual[3][2]+estado_atual[3][3]} \033[m|\033[1;37;42m {estado_atual[3][4]+estado_atual[3][5]} \033[m|\033[1;37;44m {estado_atual[0][0]+estado_atual[0][1]} \033[m|\033[1;37;44m {estado_atual[0][2]+estado_atual[0][3]} \033[m|\033[1;37;44m {estado_atual[0][4]+estado_atual[0][5]} \033[m|\033[1;37;45m {estado_atual[2][0]+estado_atual[2][1]} \033[m|\033[1;37;45m {estado_atual[2][2]+estado_atual[2][3]} \033[m|\033[1;37;45m {estado_atual[2][4]+estado_atual[2][5]} \033[m|\033[0;37;41m {estado_atual[1][0]+estado_atual[1][1]} \033[m|\033[0;37;41m {estado_atual[1][2]+estado_atual[1][3]} \033[m|\033[0;37;41m {estado_atual[1][4]+estado_atual[1][5]} \033[m|")
  print(f"|\033[1;37;42m {estado_atual[3][6]+estado_atual[3][7]} \033[m|\033[1;37;42m {estado_atual[3][8]+estado_atual[3][9]} \033[m|\033[1;37;42m {estado_atual[3][10]+estado_atual[3][11]} \033[m|\033[1;37;44m {estado_atual[0][6]+estado_atual[0][7]} \033[m|\033[1;37;44m {estado_atual[0][8]+estado_atual[0][9]} \033[m|\033[1;37;44m {estado_atual[0][10]+estado_atual[0][11]} \033[m|\033[1;37;45m {estado_atual[2][6]+estado_atual[2][7]} \033[m|\033[1;37;45m {estado_atual[2][8]+estado_atual[2][9]} \033[m|\033[1;37;45m {estado_atual[2][10]+estado_atual[2][11]} \033[m|\033[0;37;41m {estado_atual[1][6]+estado_atual[1][7]} \033[m|\033[0;37;41m {estado_atual[1][8]+estado_atual[1][9]} \033[m|\033[0;37;41m {estado_atual[1][10]+estado_atual[1][11]} \033[m|")
  print(f"|\033[1;37;42m {estado_atual[3][12]+estado_atual[3][13]} \033[m|\033[1;37;42m {estado_atual[3][14]+estado_atual[3][15]} \033[m|\033[1;37;42m {estado_atual[3][16]+estado_atual[3][17]} \033[m|\033[1;37;44m {estado_atual[0][12]+estado_atual[0][13]} \033[m|\033[1;37;44m {estado_atual[0][14]+estado_atual[0][15]} \033[m|\033[1;37;44m {estado_atual[0][16]+estado_atual[0][17]} \033[m|\033[1;37;45m {estado_atual[2][12]+estado_atual[2][13]} \033[m|\033[1;37;45m {estado_atual[2][14]+estado_atual[2][15]} \033[m|\033[1;37;45m {estado_atual[2][16]+estado_atual[2][17]} \033[m|\033[0;37;41m {estado_atual[1][12]+estado_atual[1][13]} \033[m|\033[0;37;41m {estado_atual[1][14]+estado_atual[1][15]} \033[m|\033[0;37;41m {estado_atual[1][16]+estado_atual[1][17]} \033[m|")
  print(f"               |\033[7;37;40m {estado_atual[5][0]+estado_atual[5][1]} \033[m|\033[7;37;40m {estado_atual[5][2]+estado_atual[5][3]} \033[m|\033[7;37;40m {estado_atual[5][4]+estado_atual[5][5]} \033[m|                        ")
  print(f"               |\033[7;37;40m {estado_atual[5][6]+estado_atual[5][7]} \033[m|\033[7;37;40m {estado_atual[5][8]+estado_atual[5][9]} \033[m|\033[7;37;40m {estado_atual[5][10]+estado_atual[5][11]} \033[m|                        ")
  print(f"               |\033[7;37;40m {estado_atual[5][12]+estado_atual[5][13]} \033[m|\033[7;37;40m {estado_atual[5][14]+estado_atual[5][14]} \033[m|\033[7;37;40m {estado_atual[5][16]+estado_atual[5][17]} \033[m|                        ")