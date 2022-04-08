'''
def vm(texto):
    print(f"\033[0;37;41m{ texto }\033[m")
def az(texto):
    print(f"\033[1;37;44m{ texto }\033[m")
def vd(texto):
    print(f"\033[1;37;42m{ texto }\033[m")
def am(texto):
    print(f"\033[1;37;43m{ texto }\033[m")
def rx(texto):
    print(f"\033[1;37;45m{ texto }\033[m")
def br(texto):
    print(f"\033[1;37;40m{ texto }\033[m")


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
'''
estado_atual = []
def resetar(estado):
    #Cada face é constituida por uma string indicando o estado de cada cubie/peça
    f = "F1F2F3F4F5F6F7F8F9"
    a = "A1A2A3A4A5A6A7A8A9"
    d = "D1D2D3D4D5D6D7D8D9"
    e = "E1E2E3E4E5E6E7E8E9"
    c = "C1C2C3C4C5C6C7C8C9"
    b = "B1B2B3B4B5B6B7B8B9"
    estado.append(f) #Aprimorar estrutura de inserção do estado
    estado.append(a)
    estado.append(d)
    estado.append(e)
    estado.append(c)
    estado.append(b)


#resetar(estado_atual) #Instancia um estado inicial, para teste. Pode ser removido ao finalizar o programa
estado = []
resetar(estado)
novo_estado = []
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
#print(novo_estado)
                    
                    
                    
                    


#Estrutura para captação dos cubies um a um
#for face in estado_atual: #Acessa a estado atual verificando cada face
#    for letra in range(0,17,2): #Acessa as posições dos cubies em cada face (itera 18 vezes puxando respectivamente a face e a posição em que o cubie deveria estar)
#        print(face[letra] + face[letra+1])

#Recebe o estado atual (um vetor com strings) e realiza o calculo da heuristica
def heuristica(estado_atual): 
    pass



def display(estado_atual):
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
    for x in range(0,3):
        if(c>0):
            c = c + 2
        print("               |", end="")
        for y in range(c,c+6,2):
            if estado_atual[4][y] == 'F':
                print(f"{azul} {estado_atual[4][y]}{estado_atual[4][y+1]} {fechamento}|", end="")
            elif estado_atual[4][y] == 'A':
                print(f"{vermelho} {estado_atual[4][y]}{estado_atual[4][y+1]} {fechamento}|", end="")
            elif estado_atual[4][y] == 'D':
                print(f"{roxo} {estado_atual[4][y]}{estado_atual[4][y+1]} {fechamento}|", end="")
            elif estado_atual[4][y] == 'E':
                print(f"{verde} {estado_atual[4][y]}{estado_atual[4][y+1]} {fechamento}|", end="")
            elif estado_atual[4][y] == 'C':
                print(f"{amarelo} {estado_atual[4][y]}{estado_atual[4][y+1]} {fechamento}|", end="")
            elif estado_atual[4][y] == 'B':
                print(f"{branco} {estado_atual[4][y]}{estado_atual[4][y+1]} {fechamento}|", end="")
        print("                       ", end="")
        print()
        c = y

    #Percorre as faces Esquerda, Frente, Direita e Atras, pintando-as
    c =0 ;
    for x in range(0,3):
        if(c>0):
            c = c + 2
        print("|", end="")
        for y in range(c,c+6,2):
            if estado_atual[3][y] == 'F':
                print(f"{azul} {estado_atual[3][y]}{estado_atual[3][y+1]} {fechamento}|", end="")
            elif estado_atual[3][y] == 'A':
                print(f"{vermelho} {estado_atual[3][y]}{estado_atual[3][y+1]} {fechamento}|", end="")
            elif estado_atual[3][y] == 'D':
                print(f"{roxo} {estado_atual[3][y]}{estado_atual[3][y+1]} {fechamento}|", end="")
            elif estado_atual[3][y] == 'E':
                print(f"{verde} {estado_atual[3][y]}{estado_atual[3][y+1]} {fechamento}|", end="")
            elif estado_atual[3][y] == 'C':
                print(f"{amarelo} {estado_atual[3][y]}{estado_atual[3][y+1]} {fechamento}|", end="")
            elif estado_atual[3][y] == 'B':
                print(f"{branco} {estado_atual[3][y]}{estado_atual[3][y+1]} {fechamento}|", end="")
        for y in range(c,c+6,2):
            if estado_atual[0][y] == 'F':
                print(f"{azul} {estado_atual[0][y]}{estado_atual[0][y+1]} {fechamento}|", end="")
            elif estado_atual[0][y] == 'A':
                print(f"{vermelho} {estado_atual[0][y]}{estado_atual[0][y+1]} {fechamento}|", end="")
            elif estado_atual[0][y] == 'D':
                print(f"{roxo} {estado_atual[0][y]}{estado_atual[0][y+1]} {fechamento}|", end="")
            elif estado_atual[0][y] == 'E':
                print(f"{verde} {estado_atual[0][y]}{estado_atual[0][y+1]} {fechamento}|", end="")
            elif estado_atual[0][y] == 'C':
                print(f"{amarelo} {estado_atual[0][y]}{estado_atual[0][y+1]} {fechamento}|", end="")
            elif estado_atual[0][y] == 'B':
                print(f"{branco} {estado_atual[0][y]}{estado_atual[0][y+1]} {fechamento}|", end="")
        for y in range(c,c+6,2):
            if estado_atual[2][y] == 'F':
                print(f"{azul} {estado_atual[2][y]}{estado_atual[2][y+1]} {fechamento}|", end="")
            elif estado_atual[2][y] == 'A':
                print(f"{vermelho} {estado_atual[2][y]}{estado_atual[2][y+1]} {fechamento}|", end="")
            elif estado_atual[2][y] == 'D':
                print(f"{roxo} {estado_atual[2][y]}{estado_atual[2][y+1]} {fechamento}|", end="")
            elif estado_atual[2][y] == 'E':
                print(f"{verde} {estado_atual[2][y]}{estado_atual[2][y+1]} {fechamento}|", end="")
            elif estado_atual[2][y] == 'C':
                print(f"{amarelo} {estado_atual[2][y]}{estado_atual[2][y+1]} {fechamento}|", end="")
            elif estado_atual[2][y] == 'B':
                print(f"{branco} {estado_atual[2][y]}{estado_atual[2][y+1]} {fechamento}|", end="")
        for y in range(c,c+6,2):
            if estado_atual[1][y] == 'F':
                print(f"{azul} {estado_atual[1][y]}{estado_atual[1][y+1]} {fechamento}|", end="")
            elif estado_atual[1][y] == 'A':
                print(f"{vermelho} {estado_atual[1][y]}{estado_atual[1][y+1]} {fechamento}|", end="")
            elif estado_atual[1][y] == 'D':
                print(f"{roxo} {estado_atual[1][y]}{estado_atual[1][y+1]} {fechamento}|", end="")
            elif estado_atual[1][y] == 'E':
                print(f"{verde} {estado_atual[1][y]}{estado_atual[1][y+1]} {fechamento}|", end="")
            elif estado_atual[1][y] == 'C':
                print(f"{amarelo} {estado_atual[1][y]}{estado_atual[1][y+1]} {fechamento}|", end="")
            elif estado_atual[1][y] == 'B':
                print(f"{branco} {estado_atual[1][y]}{estado_atual[1][y+1]} {fechamento}|", end="")
        print("                       ", end="")
        print()
        c = y

    #Percorre a face para baixo pintando-a
    c=0
    for x in range(0,3):
        if(c>0):
            c = c + 2
        print("               |", end="")
        for y in range(c,c+6,2):
            if estado_atual[5][y] == 'F':
                print(f"{azul} {estado_atual[5][y]}{estado_atual[5][y+1]} {fechamento}|", end="")
            elif estado_atual[5][y] == 'A':
                print(f"{vermelho} {estado_atual[5][y]}{estado_atual[5][y+1]} {fechamento}|", end="")
            elif estado_atual[5][y] == 'D':
                print(f"{roxo} {estado_atual[5][y]}{estado_atual[5][y+1]} {fechamento}|", end="")
            elif estado_atual[5][y] == 'E':
                print(f"{verde} {estado_atual[5][y]}{estado_atual[5][y+1]} {fechamento}|", end="")
            elif estado_atual[5][y] == 'C':
                print(f"{amarelo} {estado_atual[5][y]}{estado_atual[5][y+1]} {fechamento}|", end="")
            elif estado_atual[5][y] == 'B':
                print(f"{branco} {estado_atual[5][y]}{estado_atual[5][y+1]} {fechamento}|", end="")
        print("                       ", end="")
        print()
        c = y
    print()

#print(len(estado_atual))

def rotacionar(face, angulo):
    if(face == "f"):
        if(angulo == 90):
            print("Rotacionando frente 90")
        elif(angulo == 180):
            print("Rotacionando frente 180")
        elif(angulo == 270):
            print("Rotacionando frente 270")
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face == "a"):
        if(angulo == 90):
            print("Rotacionando atras 90")
        elif(angulo == 180):
            print("Rotacionando atras 180")
        elif(angulo == 270):
            print("Rotacionando atras 270")
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face == "d"):
        if(angulo == 90):
            print("Rotacionando direita 90")
        elif(angulo == 180):
            print("Rotacionando direita 180")
        elif(angulo == 270):
            print("Rotacionando direita 270")
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face == "e"):
        if(angulo == 90):
            print("Rotacionando esquerda 90")
        elif(angulo == 180):
            print("Rotacionando esquerda 180")
        elif(angulo == 270):
            print("Rotacionando esquerda 270")
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face == "c"):
        if(angulo == 90):
            print("Rotacionando cima 90")
        elif(angulo == 180):
            print("Rotacionando cima 180")
        elif(angulo == 270):
            print("Rotacionando cima 270")
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    elif(face == "b"):
        if(angulo == 90):
            print("Rotacionando baixo 90")
        elif(angulo == 180):
            print("Rotacionando baixo 180")
        elif(angulo == 270):
            print("Rotacionando baixo 270")
        else:
            print(f"Valor {angulo} nao e um angulo valido")
    else:
        print(f"Valor {face} nao e uma face valida")

def heuristica(estado, estado_objetivo):
    heuristica = 0

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
    #Percorre as faces somando a heuristica do estado
    for x in range(0,6): #Acessa a face
        for y in range(0,17,2): #Acessa cada letra dentro de uma face
            #Verifica se  a face do cubie no estado atual está na mesma posição do objetivo
            if estado[x][y] + estado[x][y+1] == estado_objetivo[x][y] + estado_objetivo[x][y+1]:
                heuristica = heuristica + 0
                print(f"{estado[x][y] + estado[x][y+1]} = 0")
            elif estado[x][y] in vetor1: #Não possuindo a face do cubie na sua posição objetivo verificamos se ela está em alguma posição de heuristica +1
                heuristica = heuristica + 1
                print(f"{estado[x][y] + estado[x][y+1]} = 1")
            elif estado[x][y] in vetor2: #Não possuindo a face do cubie na sua posição objetivo verificamos se ela está em alguma posição de heuristica +2
                heuristica = heuristica + 2
                print(f"{estado[x][y] + estado[x][y+1]} = 2")
            else:
                print("O cubie está em uma posição incorreta")
    return heuristica


heuristica()
#display(estado)
#print()
#display(novo_estado)
