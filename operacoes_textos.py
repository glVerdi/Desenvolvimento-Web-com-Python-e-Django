texto = "carro"
print(texto[4]) #Colocar o numero da posicao de cada letra dentro do [], começando em 0, 1, 2, 3 e 4
print(texto[-5]) #Começa de tras para frente, -1, -2, -3, -4 e -5
print(texto[:2]) #Vai da posicao 0 ate a posicao 2 menos ela, para aparecer a posicao 2 tem que ir ate o 3
print(texto[2:]) #Vai da posicao 2 ate a posicao final
print(texto[::2]) #Vai do inicio ate o fim, pulando de 2 em 2
print(texto[::-1]) #Vai da posicao -1 ate a posicao -5 invertendo a palavra 
frase = "Meu nome é 'Gabriel'" #Nao pode usar aspas simples com aspas simples, mas se pode usar \ para dizer que nao é o fim das aspas simples
print(frase)
frase1 = 'Meu nome é \n\tGabriel' #O \n serve para quebrar a linha e o \t faz um tab
print("nome" in frase1) #Quer saber se o "nome" esta dentro da frase
print("nome" not in frase1) #Quer saber se o "nome" nao esta dentro da frase1
print(len(frase)) #Conta a quantidade de caracteres que tem dentro da frase1
print(frase1.lower()) #Coloca toda a frase1 em letras minusculas
print(frase1.upper()) #Coloca toda a frase1 em letras maiusculas
print(dir(str)) #Aparece os recursos que posso usar com as strings
print(frase1.capitalize()) #Coloca a primeira letra da frase1 em maiusculo
print(frase1.split()) #Separa cada palavra de frase1 em uma lista
dados = "Gabriel;22anos;171;aries"
print(dados.split(";")) #Separa cada palavra no ; de dados em uma lista