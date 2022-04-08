class agente:
    #def __init__(self): #Não sei dizer se o agente necessita ter um cosntrutor ja que ele não possui atributos proprios.

    @classmethod
    #Define a ação do agente de se movimentar se o ambiente estiver limpo. 
    #Pode movimentar-se para a esquerda ou para direita a depender do estado atual em que se encontra. 
    #Retorna apenas um texto
    def movimentar(self, estado):
        if(estado == "A"):
            print(f"Movimentando-se para a direita")
        elif(estado == "B"):
            print(f"Movimentando-se para a esquerda")

    @classmethod
    #Define a ação do agente de limpar uma ambiente sujo. 
    #Retorna apenas um texto
    def limpar(self,estado):
        print(f"Ambiente {estado} limpo")    
#Instancia um agente da classe agente
a1 = agente()

#Mantem um looping de respostas do usuario e ações do agente
while True:
    #Mantem um looping para que os dados sejam passados de forma correta
    while True: 
        #Verifica através do input do usuário o estado atual do agente
        estado = str(input("Determine o estado atual como 'A' ou 'B' ( a / b ) \n")).strip().upper()[0]
        if(estado == "A" or estado == "B"):
            break
        else:
            print("Formato invalido, tente novamente!")
    
    while True: 
        #Verifica através do input do usuário o estado atual do agente
        situacao = str(input("Determine a situacao atual como 'sujo' ou 'limpo' ( s / l )\n")).strip().upper()[0]
        if(situacao == "S" or situacao == "L"):
            break
        else:
            print("Formato invalido, tente novamente!")

    #Caso a situação seja "sujo" ele irá limpar caso contrario se movimentar
    if(situacao == "S"):
        a1.limpar(estado)
    elif(situacao == "L"):
        a1.movimentar(estado)
    else:
        print("Situação nao identificada")