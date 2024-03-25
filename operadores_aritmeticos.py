#Operadores aritmeticos (binarios)
numero1 = 10
numero2 = 3
resultadoSoma = numero1 + numero2
print(resultadoSoma)
resultadoSubtracao = numero1 - numero2
print(resultadoSubtracao)
resultadoMultiplicacao = numero1 * numero2
print(resultadoMultiplicacao)
resultadoDivisao = numero1 / numero2
print(resultadoDivisao)
resultadoExponenciacao = numero1 ** numero2
print(resultadoExponenciacao)
resultadoModulo = numero1 % numero2 #Resto da Divisao
print(resultadoModulo)

#Operadores Unarios
valor = 10
valor += 1 #Incremento de 1
valor -= 1 #Decremento de 1
valor /= 2 #Divisao por 2
valor *= 2 #Multiplicacao por 2
print(valor)

"""Precedencia de operadore
0 - Parenteses
1 - Multiplicacao e Divisao
2 - Adicao e Subtracao
Sempre fazendo da esquerda para a direita"""
resultado1 = 2 + 2 * 2
print(resultado1)
resultado2 = 2 + 2 / 2 * 3
print(resultado2)
resultado3 = 2 + 2 * 2 / 3
print(resultado3)
resultado4 = (2 - 10) * 3
print(resultado4)
