# FIBONACCI
# Cada término se obtiene como la suma de los dos anteriores
# FIB = 0, 1, 1, 2, 3, 5, 8, 13, 21

# Leer N
# Imprimir los N primeros términos de la sucesión
# Imprimir la suma de los mismos

TERMINO1 = 0
TERMINO2 = 1
N = 7
SUMATOTAL = 1

print("Términos de Fibonacci:")
print("0")
print("1")

contador = 0
while(contador < N):
    FIB = TERMINO1 + TERMINO2
    TERMINO1 = TERMINO2
    TERMINO2 = FIB

    print(FIB)

    SUMATOTAL += FIB
    contador += 1

print("Suma total:", SUMATOTAL)