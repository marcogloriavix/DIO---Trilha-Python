
class Cachorro:  # criando a classe e seus atributos
    # Init estou construindo a classe (ou inicializando a classe)
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome=nome            #atributo
        self.cor=cor              #atributo   
        self.acordado = acordado  #atributo

#-----------------------------------------------------------------------
    #Definindo métodos (comportamentos da classe)
    def falar(self):
        print ("auau")


    # MÉTODO (COMPORTAMENTO) para "destruir" a classe após executada:
    def __del__(self):
        print ("removendo a instancia da classe.")


 # (M1) - definindo comportamento (Método) para melhor visualização do Objeto
    #representações de classe
    def __str__(self):
        return f"{self,__class__.__name__}: {', '.join ([ f'{chave}={valor}' for chave, valor 
        in self.__dict__.items()])}"


# (M2) - método M2 - depois é necessário chamar o método 
def criar_cachorro():
    # dentro do método M2, criei o meu OBJETO c2
    c2 = Cachorro ("Zeus", "Branco e Preto", False)
    print (c2.nome)

#--------------------------------------------------------------------------------------------# 


# OBJETO
c1=Cachorro ("Chappie", "amarelo")

# (M1) - representar Método de visualização do Objeto, conforme definido em M1.
print (c1)
c1.falar()

# (M2) - Chamar o método M2 
criar_cachorro()


#----------------------------------------------------------------------------------------#

print (" estou testando aqui 1")

# para "forçar" a destruição do objeto c1 (estância da class) antes do final do programa
del c1

print (" estou testando aqui 2")
print (" estou testando aqui 3")
print (" estou testando aqui 4")

#-----------------------------------------------------------------------------------------#

