# propuesto 03

print("Programna para convertir una cantidad de milimetros a metros, ")
print("y el resto en decimetros, centimetros y milimetros. ")
print(" ")

x=float(input("Ingrese cantidad en milimetros : "))

def m(a):
    
    m=int(a/1000)
    return m

print("La cantidad ingresada en metros es : {}".format(m(x)))

def dm(a):
    c=a%1000
    dm=int(c/100)
    return dm

print("La cantidad ingresada en decimetros es : {}".format(dm(x)))

def cm(a):
    c=a%100
    cm=int(c/10)
    return cm

print("La cantidad ingresada en centimetros es : {}".format(cm(x)))

def mm(a):
    c=a%10
    mm=int(c)
    return mm

print("La cantidad ingresada en milimetros es : {}".format(mm(x)))
