#propuesto 04
#Obtener el valor de c y d deacuerdo a la siguiente formula

def pnumero (a,b,c,d):
    casa=(4*(a**4)+3*(b*a)+(b**2))/((a**2)-(b**2))
    return casa

def snumero (a,b,c,d):
    dado=(3*(c**2)+a+b)/4
    return dado

a=float(input("ingrese el primer numero : "))
b=float(input("ingrese el segundo numero : "))


print("El resultado de C es : {}".format(casa(a,b,c,d)))
print("El resultado de D es: {}".format(dado(a,b,c,d)))
