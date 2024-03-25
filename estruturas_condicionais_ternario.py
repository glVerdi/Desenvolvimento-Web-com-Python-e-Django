#Estruturas condicionais - if else - se senao
idade = 16
condicao = idade >= 18
#Cranca, adolescente e adulto
if idade <= 13:#Inicio do bloco de codigo
    print("Criança")
elif idade <= 18:#else if
    print("Adolescente")
else:
    print("Adulto")

#Operadores ternarios
idade1 = 50
resultado = ('Menor idade', 'Maior idade')[idade >= 18] #testa se é verdadeiro e exibe o que esta mais perto da condicao
resultado1 = 'Maior idade' if idade >= 18 else 'Menor idade'
print(resultado)