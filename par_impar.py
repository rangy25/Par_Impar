# Ejercicio No.4 programa para verificar si un numero es par o impar

#input
x=int(input(" digite el valor de x: "))

#processing
R= x%2
if R==0:
    rta="par"
else:
    rta="impar"
    
#output
print(" el numero " + str (x) + " es " + rta)
    