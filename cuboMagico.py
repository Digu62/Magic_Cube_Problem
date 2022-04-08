from random import randint



def explicação():
    print("Explicação do fluxo do código:\nO algoritmo seque uma busca A* utilizando uma heuristica baseada na distancia de Manhattan. Sua função de custo é calculada por F(n) = g(n) + h(n), sendo g(n) o custo acumulado de h(n) do estado inicial até o estado atual e h(n) o custo da heuristica avaliado de acordo com os cubos de canto e sua distancia para as posições de origem, classificando seus valores de heuristica como 0 quando estão ná posição objetivo e 1 ou 2 quando estão em determinadas posições do cubo.\nO Código segue um determinado fluxo. Iniciando a busca A* pela raiz (estado embaralhado), ele verifica constantemente se alcançou o objetivo e se ainda existem elementos a serem explorados na fronteira. Com isso ele passa a gerar nós sucessores que correspondem aos 18 movimentos possíveis realizados pelo cubo, sendo capaz de rotacionar qualquer uma das 6 faces em até três graus diferentes.\nOs nós sucessores são armazenados na lista fronteira que se manter ordenada de forma crescente em relação aos custo F(n) dos estados contidos nela. Os nós aprofundados são sempre retirados do inicio da fronteira, os quais também são armazenados na lista caminho que é impressa ao se encontrar a solução.\n\n Autores:\nRodrigo Matos Peixoto\n Bruno Santos Junqueira")


#Função que leva o estado passado para o estado solucionado
def resetar(estado):
    #Cada face é constituida por uma string indicando o estado de cada cubie/peça
    f = "F1F2F3F4F5F6F7F8F9"
    a = "A1A2A3A4A5A6A7A8A9"
    d = "D1D2D3D4D5D6D7D8D9"
    e = "E1E2E3E4E5E6E7E8E9"
    c = "C1C2C3C4C5C6C7C8C9"
    b = "B1B2B3B4B5B6B7B8B9"
    gn = 0 #Armagena o custo g da raiz até o objetivo
    fn = 0 #Armazena o custo total da heuristica para este estado
    estado.append(f)
    estado.append(a)
    estado.append(d)
    estado.append(e)
    estado.append(c)
    estado.append(b)
    estado.append(gn)
    estado.append(fn)




#Recebe o estado do cubo e o exibe
def display(estado):
    #cores
    amarelo = "\033[1;37;43m"
    verde = "\033[1;37;42m"
    azul = "\033[1;37;44m"
    roxo = "\033[1;37;45m"
    vermelho = "\033[0;37;41m"
    branco = "\033[7;37;40m"
    fechamento = "\033[m"
    
    #Percorre a face cima printando ela
    c = 0
    for x in range(0,3): #Gera as linhas da face
        if(c>0):
            c = c + 2
        print("               |", end="")
        for y in range(c,c+6,2): #Gera as colunas da face analisando e adequando as cores
            if estado[4][y] == 'F':
                print(f"{azul} {estado[4][y]}{estado[4][y+1]} {fechamento}|", end="")
            elif estado[4][y] == 'A':
                print(f"{vermelho} {estado[4][y]}{estado[4][y+1]} {fechamento}|", end="")
            elif estado[4][y] == 'D':
                print(f"{roxo} {estado[4][y]}{estado[4][y+1]} {fechamento}|", end="")
            elif estado[4][y] == 'E':
                print(f"{verde} {estado[4][y]}{estado[4][y+1]} {fechamento}|", end="")
            elif estado[4][y] == 'C':
                print(f"{amarelo} {estado[4][y]}{estado[4][y+1]} {fechamento}|", end="")
            elif estado[4][y] == 'B':
                print(f"{branco} {estado[4][y]}{estado[4][y+1]} {fechamento}|", end="")
        print("                       ", end="")
        print()
        c = y

    #Percorre as faces Esquerda, Frente, Direita e Atras, pintando-as
    c =0 ;
    for x in range(0,3): #Gera as linhas das faces
        if(c>0):
            c = c + 2
        print("|", end="")
        for y in range(c,c+6,2):#Gera as colunas da face analisando e adequando as cores
            if estado[3][y] == 'F':
                print(f"{azul} {estado[3][y]}{estado[3][y+1]} {fechamento}|", end="")
            elif estado[3][y] == 'A':
                print(f"{vermelho} {estado[3][y]}{estado[3][y+1]} {fechamento}|", end="")
            elif estado[3][y] == 'D':
                print(f"{roxo} {estado[3][y]}{estado[3][y+1]} {fechamento}|", end="")
            elif estado[3][y] == 'E':
                print(f"{verde} {estado[3][y]}{estado[3][y+1]} {fechamento}|", end="")
            elif estado[3][y] == 'C':
                print(f"{amarelo} {estado[3][y]}{estado[3][y+1]} {fechamento}|", end="")
            elif estado[3][y] == 'B':
                print(f"{branco} {estado[3][y]}{estado[3][y+1]} {fechamento}|", end="")
        for y in range(c,c+6,2):
            if estado[0][y] == 'F':
                print(f"{azul} {estado[0][y]}{estado[0][y+1]} {fechamento}|", end="")
            elif estado[0][y] == 'A':
                print(f"{vermelho} {estado[0][y]}{estado[0][y+1]} {fechamento}|", end="")
            elif estado[0][y] == 'D':
                print(f"{roxo} {estado[0][y]}{estado[0][y+1]} {fechamento}|", end="")
            elif estado[0][y] == 'E':
                print(f"{verde} {estado[0][y]}{estado[0][y+1]} {fechamento}|", end="")
            elif estado[0][y] == 'C':
                print(f"{amarelo} {estado[0][y]}{estado[0][y+1]} {fechamento}|", end="")
            elif estado[0][y] == 'B':
                print(f"{branco} {estado[0][y]}{estado[0][y+1]} {fechamento}|", end="")
        for y in range(c,c+6,2):
            if estado[2][y] == 'F':
                print(f"{azul} {estado[2][y]}{estado[2][y+1]} {fechamento}|", end="")
            elif estado[2][y] == 'A':
                print(f"{vermelho} {estado[2][y]}{estado[2][y+1]} {fechamento}|", end="")
            elif estado[2][y] == 'D':
                print(f"{roxo} {estado[2][y]}{estado[2][y+1]} {fechamento}|", end="")
            elif estado[2][y] == 'E':
                print(f"{verde} {estado[2][y]}{estado[2][y+1]} {fechamento}|", end="")
            elif estado[2][y] == 'C':
                print(f"{amarelo} {estado[2][y]}{estado[2][y+1]} {fechamento}|", end="")
            elif estado[2][y] == 'B':
                print(f"{branco} {estado[2][y]}{estado[2][y+1]} {fechamento}|", end="")
        for y in range(c,c+6,2):
            if estado[1][y] == 'F':
                print(f"{azul} {estado[1][y]}{estado[1][y+1]} {fechamento}|", end="")
            elif estado[1][y] == 'A':
                print(f"{vermelho} {estado[1][y]}{estado[1][y+1]} {fechamento}|", end="")
            elif estado[1][y] == 'D':
                print(f"{roxo} {estado[1][y]}{estado[1][y+1]} {fechamento}|", end="")
            elif estado[1][y] == 'E':
                print(f"{verde} {estado[1][y]}{estado[1][y+1]} {fechamento}|", end="")
            elif estado[1][y] == 'C':
                print(f"{amarelo} {estado[1][y]}{estado[1][y+1]} {fechamento}|", end="")
            elif estado[1][y] == 'B':
                print(f"{branco} {estado[1][y]}{estado[1][y+1]} {fechamento}|", end="")
        print("                       ", end="")
        print()
        c = y

    #Percorre a face para baixo pintando-a
    c=0
    for x in range(0,3): #Gera as linhas da face
        if(c>0):
            c = c + 2
        print("               |", end="")
        for y in range(c,c+6,2):#Gera as colunas da face analisando e adequando as cores
            if estado[5][y] == 'F':
                print(f"{azul} {estado[5][y]}{estado[5][y+1]} {fechamento}|", end="")
            elif estado[5][y] == 'A':
                print(f"{vermelho} {estado[5][y]}{estado[5][y+1]} {fechamento}|", end="")
            elif estado[5][y] == 'D':
                print(f"{roxo} {estado[5][y]}{estado[5][y+1]} {fechamento}|", end="")
            elif estado[5][y] == 'E':
                print(f"{verde} {estado[5][y]}{estado[5][y+1]} {fechamento}|", end="")
            elif estado[5][y] == 'C':
                print(f"{amarelo} {estado[5][y]}{estado[5][y+1]} {fechamento}|", end="")
            elif estado[5][y] == 'B':
                print(f"{branco} {estado[5][y]}{estado[5][y+1]} {fechamento}|", end="")
        print("                       ", end="")
        print()
        c = y
    print()

#Realiza as ações de rotação passando-se um estado, face e angulo.
def rotacionar(estado, face, angulo):
    novo_estado =[]
    if(face.upper() == "F"):
        if(angulo == 90):
            #Rotacionando F e reposionando no novo estado
            novo_estado.append(estado[0][12] + estado[0][13] + estado[0][6] + estado[0][7] + estado[0][0] + estado[0][1] + estado[0][14] + estado[0][15] + estado[0][8] + estado[0][9] + estado[0][2] + estado[0][3] + estado[0][16] + estado[0][17] + estado[0][10] + estado[0][11] + estado[0][4] + estado[0][5])
            # Atras se mantem normal
            novo_estado.append(estado[1])
            #O lado direito agora passa a receber alguns valores de cima 
            novo_estado.append(estado[4][12] + estado[4][13] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[4][14] + estado[4][15] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[4][16] + estado[4][17] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #O lado esquerdo agora passa a receber alguns valores de baixo
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[5][0] + estado[5][1] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[5][2] + estado[5][3] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[5][4] + estado[5][5])
            #Cima agora recebe alguns dos valores da esquerda
            novo_estado.append(estado[4][0] + estado[4][1] + estado[4][2] + estado[4][3] + estado[4][4] + estado[4][5] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[3][16] + estado[3][17] + estado[3][10] + estado[3][11] + estado[3][4] + estado[3][5])
            #O estado de baixo recebe alguns valores da direita
            novo_estado.append(estado[2][12] + estado[2][13] + estado[2][6] + estado[2][7] + estado[2][0] + estado[2][1] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[5][12] + estado[5][13] + estado[5][14] + estado[5][15] + estado[5][16] + estado[5][17])
        elif(angulo == 180):
            #Rotacionando F e reposionando no novo estado
            novo_estado.append(estado[0][16] + estado[0][17] + estado[0][14] + estado[0][15] + estado[0][12] + estado[0][13] + estado[0][10] + estado[0][11] + estado[0][8] + estado[0][9] + estado[0][6] + estado[0][7] + estado[0][4] + estado[0][5] + estado[0][2] + estado[0][3] + estado[0][0] + estado[0][1])
            # Atras se mantem normal
            novo_estado.append(estado[1])
            #O lado direito agora passa a receber alguns valores do lado esquerdo
            novo_estado.append(estado[3][16] + estado[3][17] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[3][10] + estado[3][11] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[3][4] + estado[4][5] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #O lado esquerdo agora passa a receber alguns valores do lado direito
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[2][12] + estado[2][13] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[2][6] + estado[2][7] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[2][0] + estado[2][1])
            #Cima agora recebe alguns dos valores de baixo
            novo_estado.append(estado[4][0] + estado[4][1] + estado[4][2] + estado[4][3] + estado[4][4] + estado[4][5] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[5][4] + estado[5][5] + estado[5][2] + estado[5][3] + estado[5][0] + estado[5][1])
            #O estado de baixo recebe alguns valores de cima
            novo_estado.append(estado[4][16] + estado[4][17] + estado[4][14] + estado[4][15] + estado[4][12] + estado[4][13] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[5][12] + estado[5][13] + estado[5][14] + estado[5][15] + estado[5][16] + estado[5][17])
        elif(angulo == 270):
            #Rotacionando F e reposionando no novo estado
            novo_estado.append(estado[0][4] + estado[0][5] + estado[0][10] + estado[0][11] + estado[0][16] + estado[0][17] + estado[0][2] + estado[0][3] + estado[0][8] + estado[0][9] + estado[0][14] + estado[0][15] + estado[0][0] + estado[0][1] + estado[0][6] + estado[0][7] + estado[0][12] + estado[0][13])
            # Atras se mantem normal
            novo_estado.append(estado[1])
            #O lado direito agora passa a receber alguns valores de baixo
            novo_estado.append(estado[5][4] + estado[5][5] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[5][2] + estado[5][3] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[5][0] + estado[5][1] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #O lado esquerdo agora passa a receber alguns valores de cima
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[4][16] + estado[4][17] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[4][14] + estado[4][15] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[4][12] + estado[4][13])
            #Cima agora recebe alguns dos valores da direita
            novo_estado.append(estado[4][0] + estado[4][1] + estado[4][2] + estado[4][3] + estado[4][4] + estado[4][5] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[2][0] + estado[2][1] + estado[2][6] + estado[2][7] + estado[2][12] + estado[2][13])
            #O estado de baixo recebe alguns valores da esquerda
            novo_estado.append(estado[3][4] + estado[3][5] + estado[3][10] + estado[3][11] + estado[3][16] + estado[3][17] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[5][12] + estado[5][13] + estado[5][14] + estado[5][15] + estado[5][16] + estado[5][17])
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face.upper() == "A"):
        if(angulo == 90):
            #A frente se mantem intacta
            novo_estado.append(estado[0])
            #Atras rotaciona
            novo_estado.append(estado[1][12] + estado[1][13] + estado[1][6] + estado[1][7] + estado[1][0] + estado[1][1] + estado[1][14] + estado[1][15] + estado[1][8] + estado[1][9] + estado[1][2] + estado[1][3] + estado[1][16] + estado[1][17] + estado[1][10] + estado[1][11] + estado[1][4] + estado[1][5])
            #O lado direito agora passa a receber alguns valores de baixo 
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[5][16] + estado[5][17] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[5][14] + estado[5][15] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[5][12] + estado[5][13])
            #O lado esquerdo agora passa a receber alguns valores de cima
            novo_estado.append(estado[4][4] + estado[4][5] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[4][2] + estado[4][3] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[4][0] + estado[4][1] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #Cima agora recebe alguns dos valores da direita
            novo_estado.append(estado[2][4] + estado[2][5] + estado[2][10] + estado[2][11] + estado[2][16] + estado[2][17] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[4][12] + estado[4][13] + estado[4][14] + estado[4][15] + estado[4][16] + estado[4][17])
            #O estado de baixo recebe alguns valores da esquerda
            novo_estado.append(estado[5][0] + estado[5][1] + estado[5][2] + estado[5][3] + estado[5][4] + estado[5][5] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[3][0] + estado[3][1] + estado[3][6] + estado[3][7] + estado[3][12] + estado[3][13])
        elif(angulo == 180):
            #A frente se mantem intacta
            novo_estado.append(estado[0])
            #Atras rotaciona
            novo_estado.append(estado[1][16] + estado[1][17] + estado[1][14] + estado[1][15] + estado[1][12] + estado[1][13] + estado[1][10] + estado[1][11] + estado[1][8] + estado[1][9] + estado[1][6] + estado[1][7] + estado[1][4] + estado[1][5] + estado[1][2] + estado[1][3] + estado[1][0] + estado[1][1])
            #O lado direito agora passa a receber alguns valores do esquerdo
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[3][12] + estado[3][13] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[3][6] + estado[3][7] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[3][0] + estado[3][1])
            #O lado esquerdo agora passa a receber alguns valores do direito
            novo_estado.append(estado[2][16] + estado[2][17] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[2][10] + estado[2][11] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[2][4] + estado[2][5] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #Cima agora recebe alguns dos valores de baixo
            novo_estado.append(estado[5][16] + estado[5][17] + estado[5][14] + estado[5][15] + estado[5][12] + estado[5][13] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[4][12] + estado[4][13] + estado[4][14] + estado[4][15] + estado[4][16] + estado[4][17])
            #O estado de baixo recebe alguns valores de cima
            novo_estado.append(estado[5][0] + estado[5][1] + estado[5][2] + estado[5][3] + estado[5][4] + estado[5][5] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[4][4] + estado[4][5] + estado[4][2] + estado[4][3] + estado[4][0] + estado[4][1])
        elif(angulo == 270):
            #A frente se mantem intacta
            novo_estado.append(estado[0])
            #Atras rotaciona
            novo_estado.append(estado[1][4] + estado[1][5] + estado[1][10] + estado[1][11] + estado[1][16] + estado[1][17] + estado[1][2] + estado[1][3] + estado[1][8] + estado[1][9] + estado[1][14] + estado[1][15] + estado[1][0] + estado[1][1] + estado[1][6] + estado[1][7] + estado[1][12] + estado[1][13])
            #O lado direito agora passa a receber alguns valores de cima 
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[4][0] + estado[4][1] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[4][2] + estado[4][3] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[4][4] + estado[4][5])
            #O lado esquerdo agora passa a receber alguns valores de baixo
            novo_estado.append(estado[5][12] + estado[5][13] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[5][14] + estado[5][15] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[5][16] + estado[5][17] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #Cima agora recebe alguns dos valores da esquerda
            novo_estado.append(estado[3][12] + estado[3][13] + estado[3][6] + estado[3][7] + estado[3][0] + estado[3][1] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[4][12] + estado[4][13] + estado[4][14] + estado[4][15] + estado[4][16] + estado[4][17])
            #O estado de baixo recebe alguns valores direita
            novo_estado.append(estado[5][0] + estado[5][1] + estado[5][2] + estado[5][3] + estado[5][4] + estado[5][5] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[2][16] + estado[2][17] + estado[2][10] + estado[2][11] + estado[2][4] + estado[2][5])
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face.upper() == "D"):
        if(angulo == 90):
            #Frente recebe alguns valores de baixo
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[5][4] + estado[5][5] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[5][10] + estado[5][11] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[5][16] + estado[5][17])
            #Atras rebe alguns valores de cima
            novo_estado.append(estado[4][16] + estado[4][17] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[4][10] + estado[4][11] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[4][4] + estado[4][5] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #O lado direito rotaciona
            novo_estado.append(estado[2][12] + estado[2][13] + estado[2][6] + estado[2][7] + estado[2][0] + estado[2][1] + estado[2][14] + estado[2][15] + estado[2][8] + estado[2][9] + estado[2][2] + estado[2][3] + estado[2][16] + estado[2][17] + estado[2][10] + estado[2][11] + estado[2][4] + estado[2][5])
            #O lado esquerdo se mantem intacto
            novo_estado.append(estado[3])
            #Cima agora recebe alguns dos valores da frente
            novo_estado.append(estado[4][0] + estado[4][1] + estado[4][2] + estado[4][3] + estado[0][4] + estado[0][5] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[0][10] + estado[0][11] + estado[4][12] + estado[4][13] + estado[4][14] + estado[4][15] + estado[0][16] + estado[0][17])
            #O estado de baixo recebe alguns valores de tras
            novo_estado.append(estado[5][0] + estado[5][1] + estado[5][2] + estado[5][3] + estado[1][12] + estado[1][13] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[1][6] + estado[1][7] + estado[5][12] + estado[5][13] + estado[5][14] + estado[5][15] + estado[1][0] + estado[1][1])
        elif(angulo == 180):
            #Frente recebe alguns valores de tras
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[1][12] + estado[1][13] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[1][6] + estado[1][7] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[1][0] + estado[1][1])
            #Atras rebe alguns valores da frente
            novo_estado.append(estado[0][16] + estado[0][17] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[0][10] + estado[0][11] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[0][4] + estado[0][5] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #O lado direito rotaciona
            novo_estado.append(estado[2][16] + estado[2][17] + estado[2][14] + estado[2][15] + estado[2][12] + estado[2][13] + estado[2][10] + estado[2][11] + estado[2][8] + estado[2][9] + estado[2][6] + estado[2][7] + estado[2][4] + estado[2][5] + estado[2][2] + estado[2][3] + estado[2][0] + estado[2][1])
            #O lado esquerdo se mantem intacto
            novo_estado.append(estado[3])
            #Cima agora recebe alguns dos valores de baixo
            novo_estado.append(estado[4][0] + estado[4][1] + estado[4][2] + estado[4][3] + estado[5][4] + estado[5][5] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[5][10] + estado[5][11] + estado[4][12] + estado[4][13] + estado[4][14] + estado[4][15] + estado[5][16] + estado[5][17])
            #O estado de baixo recebe alguns valores de cima
            novo_estado.append(estado[5][0] + estado[5][1] + estado[5][2] + estado[5][3] + estado[4][4] + estado[4][5] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[4][10] + estado[4][11] + estado[5][12] + estado[5][13] + estado[5][14] + estado[5][15] + estado[4][16] + estado[4][17])
        elif(angulo == 270):
            #Frente recebe alguns valores de cima
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[4][4] + estado[4][5] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[4][10] + estado[4][11] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[4][16] + estado[4][17])
            #Atras rebe alguns valores de baixo
            novo_estado.append(estado[5][16] + estado[5][17] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[5][10] + estado[5][11] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[5][4] + estado[5][5] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #O lado direito rotaciona
            novo_estado.append(estado[2][4] + estado[2][5] + estado[2][10] + estado[2][11] + estado[2][16] + estado[2][17] + estado[2][2] + estado[2][3] + estado[2][8] + estado[2][9] + estado[2][14] + estado[2][15] + estado[2][0] + estado[2][1] + estado[2][6] + estado[2][7] + estado[2][12] + estado[2][13])
            #O lado esquerdo se mantem intacto
            novo_estado.append(estado[3])
            #Cima agora recebe alguns dos valores de tras
            novo_estado.append(estado[4][0] + estado[4][1] + estado[4][2] + estado[4][3] + estado[1][12] + estado[1][13] + estado[4][6] + estado[4][7] + estado[4][8] + estado[4][9] + estado[1][6] + estado[1][7] + estado[4][12] + estado[4][13] + estado[4][14] + estado[4][15] + estado[1][0] + estado[1][1])
            #O estado de baixo recebe alguns valores da frente
            novo_estado.append(estado[5][0] + estado[5][1] + estado[5][2] + estado[5][3] + estado[0][4] + estado[0][5] + estado[5][6] + estado[5][7] + estado[5][8] + estado[5][9] + estado[0][10] + estado[0][11] + estado[5][12] + estado[5][13] + estado[5][14] + estado[5][15] + estado[0][16] + estado[0][17])
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face.upper() == "E"):
        if(angulo == 90):
            #Frente recebe alguns valores de cima
            novo_estado.append(estado[4][0] + estado[4][1] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[4][6] + estado[4][7] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[4][12] + estado[4][13] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #Atras rebe alguns valores de baixo
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[5][12] + estado[5][13] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[5][6] + estado[5][7] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[5][0] + estado[5][1])
            #O lado direito se mantem intacto
            novo_estado.append(estado[2])
            #O lado esquerdo rotaciona
            novo_estado.append(estado[3][12] + estado[3][13] + estado[3][6] + estado[3][7] + estado[3][0] + estado[3][1] + estado[3][14] + estado[3][15] + estado[3][8] + estado[3][9] + estado[3][2] + estado[3][3] + estado[3][16] + estado[3][17] + estado[3][10] + estado[3][11] + estado[3][4] + estado[3][5])
            #Cima agora recebe alguns dos valores de tras
            novo_estado.append(estado[1][16] + estado[1][17] + estado[4][2] + estado[4][3] + estado[4][4] + estado[4][5] + estado[1][10] + estado[1][11] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[1][4] + estado[1][5] + estado[4][14] + estado[4][15] + estado[4][16] + estado[4][17])
            #O estado de baixo recebe alguns valores da frente
            novo_estado.append(estado[0][0] + estado[0][1] + estado[5][2] + estado[5][3] + estado[5][4] + estado[5][5] + estado[0][6] + estado[0][7] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[0][12] + estado[0][13] + estado[5][14] + estado[5][15] + estado[5][16] + estado[5][17])
        elif(angulo == 180):
            #Frente recebe alguns valores de tras
            novo_estado.append(estado[1][16] + estado[1][17] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[1][10] + estado[1][11] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[1][4] + estado[1][5] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #Atras rebe alguns valores da frente
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[0][12] + estado[0][13] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[0][6] + estado[0][7] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[0][0] + estado[0][1])
            #O lado direito se mantem intacto
            novo_estado.append(estado[2])
            #O lado esquerdo rotaciona
            novo_estado.append(estado[3][16] + estado[3][17] + estado[3][14] + estado[3][15] + estado[3][12] + estado[3][13] + estado[3][10] + estado[3][11] + estado[3][8] + estado[3][9] + estado[3][6] + estado[3][7] + estado[3][4] + estado[3][5] + estado[3][2] + estado[3][3] + estado[3][0] + estado[3][1])
            #Cima agora recebe alguns dos valores de baixo
            novo_estado.append(estado[5][0] + estado[5][1] + estado[4][2] + estado[4][3] + estado[4][4] + estado[4][5] + estado[5][6] + estado[5][7] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[5][12] + estado[5][13] + estado[4][14] + estado[4][15] + estado[4][16] + estado[4][17])
            #O estado de baixo recebe alguns valores de cima
            novo_estado.append(estado[4][0] + estado[4][1] + estado[5][2] + estado[5][3] + estado[5][4] + estado[5][5] + estado[4][6] + estado[4][7] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[4][12] + estado[4][13] + estado[5][14] + estado[5][15] + estado[5][16] + estado[5][17])
        elif(angulo == 270):
            #Frente recebe alguns valores de baixo
            novo_estado.append(estado[5][0] + estado[5][1] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[5][6] + estado[5][7] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[5][12] + estado[5][13] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #Atras rebe alguns valores de cima
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[4][12] + estado[4][13] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[4][6] + estado[4][7] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[4][0] + estado[4][1])
            #O lado direito se mantem intacto
            novo_estado.append(estado[2])
            #O lado esquerdo rotaciona
            novo_estado.append(estado[3][4] + estado[3][5] + estado[3][10] + estado[3][11] + estado[3][16] + estado[3][17] + estado[3][2] + estado[3][3] + estado[3][8] + estado[3][9] + estado[3][14] + estado[3][15] + estado[3][0] + estado[3][1] + estado[3][6] + estado[3][7] + estado[3][12] + estado[3][13])
            #Cima agora recebe alguns dos valores da frente
            novo_estado.append(estado[0][0] + estado[0][1] + estado[4][2] + estado[4][3] + estado[4][4] + estado[4][5] + estado[0][6] + estado[0][7] + estado[4][8] + estado[4][9] + estado[4][10] + estado[4][11] + estado[0][12] + estado[0][13] + estado[4][14] + estado[4][15] + estado[4][16] + estado[4][17])
            #O estado de baixo recebe alguns valores de tras
            novo_estado.append(estado[1][16] + estado[1][17] + estado[5][2] + estado[5][3] + estado[5][4] + estado[5][5] + estado[1][10] + estado[1][11] + estado[5][8] + estado[5][9] + estado[5][10] + estado[5][11] + estado[1][4] + estado[1][5] + estado[5][14] + estado[5][15] + estado[5][16] + estado[5][17])
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face.upper() == "C"):
        if(angulo == 90):
            #Frente recebe alguns valores de direita
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #Atras recebe alguns valores de esquerda
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #O lado direito agora passa a receber alguns valores de tras 
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #O lado esquerdo agora passa a receber alguns valores da frente
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #Cima rotaciona
            novo_estado.append(estado[4][12] + estado[4][13] + estado[4][6] + estado[4][7] + estado[4][0] + estado[4][1] + estado[4][14] + estado[4][15] + estado[4][8] + estado[4][9] + estado[4][2] + estado[4][3] + estado[4][16] + estado[4][17] + estado[4][10] + estado[4][11] + estado[4][4] + estado[4][5])
            #O estado de baixo se mantem intacto
            novo_estado.append(estado[5])
        elif(angulo == 180):
            #Frente recebe alguns valores de tras
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #Atras recebe alguns valores da frente
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #O lado direito agora passa a receber alguns valores do esquerdo
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #O lado esquerdo agora passa a receber alguns valores do direito
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #Cima rotaciona
            novo_estado.append(estado[4][16] + estado[4][17] + estado[4][14] + estado[4][15] + estado[4][12] + estado[4][13] + estado[4][10] + estado[4][11] + estado[4][8] + estado[4][9] + estado[4][6] + estado[4][7] + estado[4][4] + estado[4][5] + estado[4][2] + estado[4][3] + estado[4][0] + estado[4][1])
            #O estado de baixo se mantem intacto
            novo_estado.append(estado[5])
        elif(angulo == 270):
            #Frente recebe alguns valores da esquerda
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #Atras recebe alguns valores da direita
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #Direito recebee alguns valores da frente
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #Esquerdo recebee alguns valores do atras
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #Cima rotaciona
            novo_estado.append(estado[4][4] + estado[4][5] + estado[4][10] + estado[4][11] + estado[4][16] + estado[4][17] + estado[4][2] + estado[4][3] + estado[4][8] + estado[4][9] + estado[4][14] + estado[4][15] + estado[4][0] + estado[4][1] + estado[4][6] + estado[4][7] + estado[4][12] + estado[4][13])
            #O estado de baixo se mantem intacto
            novo_estado.append(estado[5])
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face.upper() == "B"):
        if(angulo == 90):
            #Frente recebe alguns valores de esquerda 
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #Atras recebe alguns valores da direita
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #O lado direito agora passa a receber alguns valores da frente
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #O lado esquerdo agora passa a receber alguns valores de tras
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #Cima se mantem intacto
            novo_estado.append(estado[4])
            #Baixo rotaciona
            novo_estado.append(estado[5][12] + estado[5][13] + estado[5][6] + estado[5][7] + estado[5][0] + estado[5][1] + estado[5][14] + estado[5][15] + estado[5][8] + estado[5][9] + estado[5][2] + estado[5][3] + estado[5][16] + estado[5][17] + estado[5][10] + estado[5][11] + estado[5][4] + estado[5][5])
        elif(angulo == 180):
            #Frente recebe alguns valores de tras
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #Atras recebe alguns valores da frente
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #O lado direito agora passa a receber alguns valores de esquerdo
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #O lado esquerdo agora passa a receber alguns valores do direito
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #Cima se mantem intacto
            novo_estado.append(estado[4])
            #Baixo rotaciona
            novo_estado.append(estado[5][16] + estado[5][17] + estado[5][14] + estado[5][15] + estado[5][12] + estado[5][13] + estado[5][10] + estado[5][11] + estado[5][8] + estado[5][9] + estado[5][6] + estado[5][7] + estado[5][4] + estado[5][5] + estado[5][2] + estado[5][3] + estado[5][0] + estado[5][1])
        elif(angulo == 270):
            #Frente recebe alguns valores de direita
            novo_estado.append(estado[0][0] + estado[0][1] + estado[0][2] + estado[0][3] + estado[0][4] + estado[0][5] + estado[0][6] + estado[0][7] + estado[0][8] + estado[0][9] + estado[0][10] + estado[0][11] + estado[2][12] + estado[2][13] + estado[2][14] + estado[2][15] + estado[2][16] + estado[2][17])
            #Atras recebe alguns valores de esquerda
            novo_estado.append(estado[1][0] + estado[1][1] + estado[1][2] + estado[1][3] + estado[1][4] + estado[1][5] + estado[1][6] + estado[1][7] + estado[1][8] + estado[1][9] + estado[1][10] + estado[1][11] + estado[3][12] + estado[3][13] + estado[3][14] + estado[3][15] + estado[3][16] + estado[3][17])
            #O lado direito agora passa a receber alguns valores de tras 
            novo_estado.append(estado[2][0] + estado[2][1] + estado[2][2] + estado[2][3] + estado[2][4] + estado[2][5] + estado[2][6] + estado[2][7] + estado[2][8] + estado[2][9] + estado[2][10] + estado[2][11] + estado[1][12] + estado[1][13] + estado[1][14] + estado[1][15] + estado[1][16] + estado[1][17])
            #O lado esquerdo agora passa a receber alguns valores da frente
            novo_estado.append(estado[3][0] + estado[3][1] + estado[3][2] + estado[3][3] + estado[3][4] + estado[3][5] + estado[3][6] + estado[3][7] + estado[3][8] + estado[3][9] + estado[3][10] + estado[3][11] + estado[0][12] + estado[0][13] + estado[0][14] + estado[0][15] + estado[0][16] + estado[0][17])
            #Cima se mantem intacto
            novo_estado.append(estado[4])
            #Baixo rotaciona
            novo_estado.append(estado[5][4] + estado[5][5] + estado[5][10] + estado[5][11] + estado[5][16] + estado[5][17] + estado[5][2] + estado[5][3] + estado[5][8] + estado[5][9] + estado[5][14] + estado[5][15] + estado[5][0] + estado[5][1] + estado[5][6] + estado[5][7] + estado[5][12] + estado[5][13])
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    else:
        print(f"Valor {face} nao e uma face valida")
    
    #Seta os valores finais do estado como o custo acumulado o g(n) acumulado do pai e f(n) = 0
    novo_estado.append(estado[6])
    f = 0 #f(n)
    novo_estado.append(f)
    return novo_estado

#Recebe o proximo estado (um vetor com strings) e realiza o calculo da heuristica retornando o f(n)
def heuristica(estado, estado_objetivo):
    hValor = 0 #h(n)

    #Vetor com posições de heuristica 1
    vetor1 =[
            estado[0][0], #f1
            estado[0][4], #f3
            estado[0][12], #f7
            estado[0][16], #f9
            estado[1][0], #A1
            estado[1][16], #A9
            estado[2][0], #D1
            estado[3][0], #f9
            estado[4][0], #C1
            estado[5][0], #B1
            ]

    #Vetor com posições de heuristica 2
    vetor2 =[
            estado[1][4], #A3
            estado[1][12], #A7
            estado[2][4], #D3
            estado[2][12], #D7
            estado[2][16], #D9
            estado[3][4], #E3
            estado[3][12], #E7
            estado[3][16], #E9
            estado[4][4], #C3
            estado[4][12], #C7
            estado[4][16], #C9
            estado[5][4], #B3
            estado[5][12], #B7
            estado[5][16], #B9
            ]
    
    #Percorre as faces somando a heuristica h(n) do estado até o estado objetivo
    for x in range(0,6): #Acessa a face
        for y in [0,4,12,16]: #Acessa apenas os cantos de cada cubie
            #Verifica se  a face do cubie no estado atual está na mesma posição do objetivo
            if estado[x][y] + estado[x][y+1] == estado_objetivo[x][y] + estado_objetivo[x][y+1]:
                hValor = hValor + 0
            elif estado[x][y] in vetor1: #Não possuindo a face do cubie na sua posição objetivo verificamos se ela está em alguma posição de heuristica +1
                hValor = hValor + 1
            elif estado[x][y] in vetor2: #Não possuindo a face do cubie na sua posição objetivo verificamos se ela está em alguma posição de heuristica +2
                hValor = hValor + 2
            else:
                print("O cubie está em uma posição incorreta")
    estado[6] += hValor #Acessa o valor g(n) acumulado do estado inicial até o atual e adiciona a ele o h(n) do estado atual
    estado[7] += estado[6] + hValor  #Acessa o valor F(n) e salva ele como a soma do g(n) + h(n)
    
    return estado[7]

#Retorna um boleano informando se o objetivo foi alcançado ou não 
def objetivoAlcancado(estado,estado_objetivo):
    for x in range(0,6): #Acessa a face
        for y in range(0,17,2): #Acessa apenas os cantos de cada cubie
            if estado[x][y] + estado[x][y+1] != estado_objetivo[x][y] + estado_objetivo[x][y+1]:
                return False
    return True

#A busca recebe um estado inicial embaralhado e atua com um looping buscando através da arvore até alcançar o objetivo ou não possuir mais nós fronteira a serem abertos
def buscaAEstrela(estado_inicial, estado_objetivo):
    estado_atual = estado_inicial #Estado que vai percorrer a arvore para verificar se encontrou o objetivo
    fronteira = [estado_inicial] #Instancia uma lista fronteira que armazenará os nós que ainda não foram explorados. Ela já inicia com o nó raiz (embaralhado) da arvore
    caminho = [] #Armazena o caminho de nós selecionados pela busca
    while len(fronteira) > 0  and not objetivoAlcancado(estado_atual, estado_objetivo): #Enquanto houverem nós na fronteira e o objetivo não for alcançado a busca deve continuar
        estado_atual = selecionaNo(estado_atual,estado_objetivo, caminho, fronteira) #Atribui a variável noSelecionado o proximo nó a ser seguido
        if objetivoAlcancado(estado_atual, estado_objetivo):
            print("Solução Encontrada")
            print()
            print("Caminho Percorrido:")
            for x in caminho:
                display(x)
        else:
            gerarSucessores(estado_atual, estado_objetivo, fronteira) #Pega o nó selecionado e gera seus sucessores
    
    if len(fronteira) == 0  and not objetivo(estado_atual, estado_objetivo):
        print("A solução não foi encontrada")

#Retorna o melhor nó, ou seja, o primeiro da lista fronteira, fazendo as devidas atualizações nela e verificando se o objetivo foi alcançado
def selecionaNo(estado_atual, estado_objetivo, caminho, fronteira):
    estado_atual = fronteira[0] #Seleciona o primeiro nó da fronteira (o de menor custo f(n))
    #Printa o estado selecionado
    caminho.append(estado_atual)
    if (objetivoAlcancado(estado_atual, estado_objetivo)):#Verifica se é o estado_objetivo foi alcançado
        return estado_atual
    fronteira.pop(0) #Remove o primeiro nó da lista fronteiro pois ele será explorado agora 
    return estado_atual #Retorna o nó escolhido

#Recebe um estado, o estado objetivo e a lista fronteira gerando seus 18 sucessores
#Faz o calculo da heuristica de cada um dos estados e os insere na fronteira
def gerarSucessores(estado, estado_objetivo, fronteira):
    #Itera valores de 0 a 5 para acessar as faces
    for x in range(0,6):
        #Itera valores de 6 a 9 para acessar os graus
        for y in range(6,9):
            novo_estado = rotacionar(estado, movimentar(x),movimentar(y))
            h = heuristica(novo_estado, estado_objetivo)
            if(len(fronteira) == 0):
                fronteira.append(novo_estado)
            else:
                #Acessa a lista fronteira verificando a ordem de f(n) e inserindo o novo_estado mantendo a ordem crescente da fronteira
                for z in range(0, len(fronteira)): #Percorre toda a lista    
                    if novo_estado[7] < fronteira[z][7]: #Se f(n) do novo estado for menor que o f(n) da fronteira ele é inserido na posição anterior
                        fronteira.insert(z,novo_estado)
                        break
                    elif(z == len(fronteira)-1): #Se estiver no ultimo elemento da lista e o f(n) ainda for maior, insere no final
                        fronteira.append(novo_estado)
                        break

#Recebe um valor e retorna a movimentação definida para ele
def movimentar(num):
    if(num == 0):
        return "F"
    elif(num == 1):
        return "A"
    elif(num == 2):
        return "D"
    elif(num == 3):
        return "E"
    elif(num == 4):
        return "C"
    elif(num == 5):
        return "B"
    elif(num == 6):
        return 90
    elif(num == 7):
        return 180
    elif(num == 8):
        return 270
    else:
        print(f"O numero {num} não é valido")

#Recebe um estado e retorna ele embaralhado X numero de vezes
def embaralhar(estado, num):
    for x in range(0, num):
        x = randint(0,5) #Escolhe a face de forma randomica
        y = randint(6,8) #Escolhe o angulo de rotação de forma randomica
        estado = rotacionar(estado, movimentar(x), movimentar(y))
        print(f"Rotacionando {movimentar(x)} {movimentar(y)} graus")
    return estado

def main():
    print("Olá, Bem vindo ao algoritmo de resolução do Cubo Mágico!")
    print()
    explicação()
    print()
    print("Esse será o formato no qual visualizaremos o cubo:")
    #instancia um estado inicial e o imprime
    estado_objetivo = []
    resetar(estado_objetivo)
    display(estado_objetivo)
    while True:
        while True:
            print("Você pode informar a quantidade de rotações que deseja para embaralhar o cubo ou embaralha-lo manualmente.")
            x = int(input("Qual você prefere? \n 1. Embaralhar automaticamente \n 2. Embaralhar Manualmente \n"))
            if x == 1:
                y = int(input("Informe quantas rotações aleatórias você deseja: "))
                estado_embaralhado = embaralhar(estado_objetivo, y)
                print("A configuração do estado embaralhado é essa:")
                display(estado_embaralhado) #Imprime o estado embaralhado
                break
            elif x == 2:
                f = str(input("Informe a face ( Frente, Atras, Direita, Esquerda, Cima, Baixo): ")).upper()[0]
                g = int(input("Informe e o grau de rotação (90, 180, 270): "))
                estado_embaralhado = rotacionar(estado_objetivo, f, g)
                display(estado_embaralhado)
                while True:
                    if str(input("Gostaria de rotacionar novamente? (Informe nao para começar a solucionar o cubo)\n")).upper()[0] == "N":
                        break
                    f = str(input("Informe a face ( Frente, Atras, Direita, Esquerda, Cima, Baixo): ")).upper()[0]
                    g = int(input("Informe e o grau de rotação (90, 180, 270): "))
                    estado_embaralhado = rotacionar(estado_embaralhado, f, g)
                    display(estado_embaralhado)
                break

            else:
                print("Valor inválido, tente novamente")

        buscaAEstrela(estado_embaralhado, estado_objetivo)

        if str(input("Gostaria de tentar novamente?\n")).upper()[0] == "N":
            break
        print("\n\n\n")
main()