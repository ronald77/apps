#propuesto 02
#Dados dos numeros enteros, determinar cuantos numeros enteros estan incluidos
#en ellos
print("Programa para calcular cuantos numeros enteros estan incluidos ")
print("de un rango de dos numeros ingresados")
print("")


def numeroent (a,b):
    numeroent=a-b-1
    return numeroent

a=int(input("ingrese el numero mayor: "))
b=int(input("ingrese el numero menor: "))



print("La cantidad de numeros enteros que hay en este rango es: {}".format(numeroent(a,b)))
