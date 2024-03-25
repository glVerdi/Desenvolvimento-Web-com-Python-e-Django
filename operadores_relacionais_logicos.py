#Operadores relacionais (retorna verdadeiro ou falso)
print(1 == 1)#Igual a
print(1 != 2)#Diferente de
print(3 > 2)#Maior que
print(1 < 2)#Menor que
print(2 >= 2)#Maior ou igual
idade = 10
print(idade <= 18)#Menor ou igual

#Operadores logicos (testa condicoes com true ou false)
print(True or True)#or (ou)
print(False or True)#or (ou)
print(False or False)#or (ou)
print(False and False)#and (e)
print(False and True)#and (e)
print(True and True)#and (e)

idade1 = 15
totalCompra = 200
resultadoOr = idade >= 50 or totalCompra >= 200
print(resultadoOr)
idade2 = 18
totalCompra1 = 200
resultadoAnd = idade >= 50 and totalCompra >= 200
print(resultadoAnd)