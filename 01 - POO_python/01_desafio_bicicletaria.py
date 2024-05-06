
# definindo Class e seus atributos:
class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor=cor         #atributo
        self.modelo= modelo  #atributo
        self.ano = ano       #atributo
        self.valor = valor   #atributo

# definindo comportamento da classe - Método   
# (MUITO CUIDADO COM A ITEMIZAÇÃO)
    def buzinar(self):
        print("Plim plim....")

    def parar(self):
        print ("parando bike")
        print ("bike parada")

    def correr(self):
        print ("vrummmm...")


    # (M1) - definindo comportamento (Método) para melhor visualização do Objeto
    #representações de classe
    def __str__(self):
        return f"{self,__class__.__name__}: {', '.join ([ f'{chave}={valor}' for chave, valor 
        in self.__dict__.items()])}"




# Objetos
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()

# chamar os atributos do meu objeto b1
print (b1.cor, b1.modelo, b1.ano, b1.valor)

# (M1) - representar Método de visualização do Objeto, conforme definido em M1.
print (b1)



