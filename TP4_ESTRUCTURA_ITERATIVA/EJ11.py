# Programa que lea un número natural H (natural = N >= 0)
# Calcular si es primo o no, e imprimir el resultado

# Leo H
# Calculo el total de nros divisores empezando por 1 (porque no se puede dividr por 0)
# Si la cantidad total de divisores es igual a 2, es primo. (2 divisores, el 1 y si mismo)

# Valores primos conocidos = 2 3 5 7 13
# (para testear)

H = 7

DIVISORES = 0
CONTADOR = 1
while(CONTADOR <= H):
    # Si el resto es 0, es divisible
    if ((H % CONTADOR) == 0):
        DIVISORES += 1

    CONTADOR += 1

if (DIVISORES == 2):
    print ("Es primo!")
else:
    print ("No es primo!")