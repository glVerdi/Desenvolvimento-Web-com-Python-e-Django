#Recursos integrados
print("Gabriel")
print(type("Gabriel"))
print(dir())
__builtins__.print("Gabriel") #Objeto que acessa um metodo

#Conversao de tipos
print(type("Gabriel")) #Str
print(type(1)) #Int
print(type(1.5)) #Float
print(type([10, 5, 9, 7])) #List
print(1 + int('2')) #Conversao da string para inteiro
print(1 + float('2.5')) #Conversao da string para float
print( '1-'+ '50') #Concatenando, colocando um do lado do outro 
numero = 9
print(str(numero) + '50') #Conversao de int para uma string e concatenando elas

#Conversao automatica
print(type(10 / 2)) #Resulta em float
print(type(2 + True)) #Resulta em e, pois o True equivale a 1 e o False equivale a 0 