#Consigo armazenar vários valores, associados a uma única variável.
#Mutáveis, consegue adicionar valores nel e depois alterá-los
#Dinâmicas aumenta de tamanho conforme adiciono elementos nela
#Heterogênea consigo armazenar vários tipos de dados 
#Indexada utiliza indices para acessar os elementos dentro dela, começa em 0

lista = ["Gabriel", "Pedro", "Ana", "João", "Maria"]
print(type(lista))
print(dir(lista))
print(lista[0]) #Acessa o primeiro elemento
print(lista[-1]) #Acessa o último elemento
print(lista[:2]) #Mostra do indice 0 até o 1
print(lista[2:5]) #Mostra do indice 2 ate o indice 4
print(lista[::2]) #Começa do indice 0 e vai de 2 em 2
#lista[0] = "Alterado"
#lista.append("Novo") #Adiciona no final da lista um novo elemento
#lista.remove("Pedro") #Remove um elemento especifico
#del lista[0] #Remove o elemento da posição 0
#print(lista[:2])
#del lista[:2]
print(len(lista)) #Mostra a quantidade de itens
print(lista.count("Gabriel")) #Mostra quantos Gabriel tem 
print(lista.index("Gabriel")) #Mostra qual é o indice de Gabriel
#lista.clear() #Limpa a lista
lista.reverse() #Inverte a ordem da lista
lista.sort() #Ordena de froma alfabetica
print("Gabriel" in lista) #Mostra se esta dentro da lista - True
print("Gabriel" not in lista) #Mostra se não esta dentro da lista - False
print(lista)