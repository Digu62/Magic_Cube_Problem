from random import randint 
from time import sleep

class agente:
    def __init__(self, estado_atual):
        self.estado_atual = estado_atual

    # O agente movimenta-se para o lado oposto ao estado  atual. Direita cado se encontre em A e esquerda caso se encontre em B
    # Após a movimentação ele atribui o novo estado no qual se encotra atualmente.
    def movimentarDireita(self):
        print(f"Movimentando-se para a direita (B)")
        self.estado_atual = "B"

    def movimentarEsquerda(self):
        print(f"Movimentando-se para a esquerda (A)")
        self.estado_atual = "A"

    #Define a ação do agente de limpar uma ambiente sujo.
    #Retorna apenas um texto
    def limpar(self):
        print(f"Limpando ambiente {self.estado_atual}")    
    
    #Utilizando a situação e estado do ambiente define qual atitude o agente deve tomar
    #Se sujo o agente limpa e se movimenta
    #Se limpo o agente apenas se moviemnta
    def decidir(self, situacao): 
        if(situacao == "S"):
            print(f"O ambiente {self.estado_atual} está sujo.")
            self.limpar()
        elif(situacao == "L"):
            print(f"O ambiente {self.estado_atual} está limpo.")
            if(self.estado_atual == "A"):
                self.movimentarDireita()
            else:
                self.movimentarEsquerda()
    
    def getEstadoAtual(self):
        return self.estado_atual




while True: 
    #Verifica através do input do usuário o estado atual do agente
    #Garante que apenas o valores "A/a" e "B/b" serão aceitos
    estado = str(input("Determine o estado atual como 'A' ou 'B' ( a / b ) \n")).strip().upper()[0]
    if(estado == "A" or estado == "B"):
        break
    else:
        print("Formato invalido, tente novamente!")

print("Para encerrar a execução insira ' -1 ' ")

#Instancia um agente da classe agente passando o estado inicial
a1 = agente(estado) 
situacao = ""
#Looping que faz o agente analisar o ambiente constantemente
#Caso o usuário digite "-" o programa é finalizado.
while (situacao != "-"):

    #Looping que garante que apenas o valores "S/s" e "L/l" serão aceitos
    while True: 
        #Verifica através do input do usuário o estado atual do agente
        situacao = str(input(f"O ambiente {a1.getEstadoAtual()} está 'sujo' ou 'limpo' ( s / l )\n")).strip().upper()[0]
        if(situacao == "S" or situacao == "L"):
            break
        elif(situacao == "-"):
            print("Execução encerrada")
            break
        else:
            print("Formato invalido, tente novamente!")
    
    a1.decidir(situacao) #Chama o agente para tomar uma recisão a partir da análise feita
    
    espere = randint(0,10) #Determina um tempo randomico de espera até a proxima consulta do ambiente
    print(f"Estou esperando {espere} segundos")
    sleep(espere) #Espera o tempo definido anteriormente antes de continuar o ciclo.
    