TypeError # genera un TypeError al sumar un numeor entero con una cadena
nume1= 5 
nume2= "3"
resultado=nume1+nume2

ZeroDivisionError #genera error al intentar dividir por 0
nume1 =10
nume2 =0 
resultado=nume1/nume2

OverflowError #genera error al exceder el limite de dato numerico
num=10.0**1000
 
IndexError # genera error  al intentar acceder a un indice que no existe
list[1,2,3]
elemnto= list[3]

KeyError # genera error al acceder a una clave que no existe en el diccionario
diccionario={"clave1,""clave2:","clave3"}
valor=diccionario["clave4"]

FileNotFoundError #genera un error si el archivo no exite en la ruta 
archivo=open("archivo.txt", "r")

ImportError #modulo cuando falla 