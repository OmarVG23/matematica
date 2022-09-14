# x=int(input("ingresa tu primer nuemero"))
# a=int(input("ingresa tu segundo numero"))
# print("La suma es",x+a)
a=[1,2,3,4,5,6,7]
print(a)
a.append(8)
# append añade un numero a la lista
print(a)
a.pop(-5)
# si dentro del parentesis se coloca -1 elimina el ultimo numero
print(a)
b=[5,2,1,3,4]
print(b)
b.sort()
# sort ordena una lista desordenada
print(b)
b.reverse()
# invierte la lista
print(b)
b.remove(5)
# quita el elementoq ue pongas en los parencteis
print(b)
# tupla inmutables no aceptan cambios se encierran dentro del parentesis y se separan conn ","
c=(1,2,1,2,3)
print(c)
c.count(2)
# count es para ver vcuantas veces se repite y entre parentesis se coloca el numero del que quieres saber la informacion
print(c.count(3))
# diccionio en python se crea una clave:valor la clave es el palabra unicay valor es significado los diccionarios so con llaves
# ejem:dicc={"gato":"cat","perro":"dog","cerdo":"pig"}
# ejem:x=input("introdce la palabra que quieres traducir en ingles :")
# ejem:print(dicc[x])

# if es alg que es ciertro o mno
edad=-5
if edad <=0:
    print("no puedes tener0")
# if-else si es verdadero if se ejecuta esto y bsi se es laso else se ejecuta esto. elif es otra opcion.
elif edad< 18:
    print("eres joven")
else:
    print("eres adulto")

# bucle for es la cantidad de veces que se repite
print("comienzo")
for i in [0,1,3,4]:
    print("hola",sep=",",end="")
print()
print("final")