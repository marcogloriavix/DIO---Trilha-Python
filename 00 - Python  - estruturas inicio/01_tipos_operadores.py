
# executar no TERMINAL em Python - clicar na seta |>   - (Run Python File)

# Operadores aritméticos
#***********************
produto_1 = 20
produto_2 = 10

print (produto_1 + produto_2)
print (produto_1 - produto_2)
print (produto_1 / produto_2)
print (produto_1 // produto_2)
print (produto_1 % produto_2)
print (produto_1 ** produto_2)


# Operadores de Comparação
#*************************
saldo =450
saque = 200
print (saldo > saque)
print (saldo <= saque)
print (saldo == saque)
print (saldo != saque)


# Operadores de Atribuição
#*************************
print("*************************")
print("Operadores de Atribuição")
saldo  = 500
print(saldo)
saldo *= 10 
print(saldo)
saldo +=200
print(saldo)
saldo -=500
print(saldo)
saldo //= 200
print(saldo)
saldo /= 10
print(saldo)
saldo %= 10
print(saldo)
saldo **=10
print(saldo)



#....

# Operadores Lógicos
#*************************
print("*************************")
print("Operadores Lógicos")

saldo =1000
saque=200
limite = 100
x=(saldo >= saque and saque <=limite)
print (x)

x=(saldo >= saque or saque <=limite)
print (x)

x=not 1000>500
print(x)

contatos_emergencia=[]
print(contatos_emergencia)

contatos_emergencia=[]
print(not contatos_emergencia)

print (True and True)
print (True and False)
print (True or True)
print (True or False)


# Operadores de Identidade
#*************************
#são operadores utilizados para comparar se os dois objetos
#testados ocupam a mesma posição na memória

print("*******************************************************")
print("Operadores de Identidade")

curso = "curso de python"
nomeCurso  = curso
saldo,limite = 200,200

x=curso is nomeCurso
print(x)

x=curso is not nomeCurso
print(x)


# Operadores de Associação
#*************************
#são operadores utilizados para verificar se um objeto está presente em uma sequencia

print("*******************************************************")
print("Operadores de Associação")

curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500,100]

print("Python" in curso)
print ("maça" not in frutas)
print (200 in saques)

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

