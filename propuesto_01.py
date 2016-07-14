#!/usr/bin/python
#Dados dos numeros enteros a y b, hallar a+b y a-b
print("Programa para hallar la suma y resta de dos números")
print("")
def suma (a,b):

	c=a+b
	
	return c
def resta (a,b):
        d=a-b
        
        return d

        
x=float(input("ingrese el Primer numero : "))
y=float(input("ingrese el Segundo numero : "))

print ("La Suma entre ",x," y ",y," es : {}".format(suma(x,y)))
print ("La Resta entre ",x,"  y ",y," es : {}".format(resta(x,y)))
