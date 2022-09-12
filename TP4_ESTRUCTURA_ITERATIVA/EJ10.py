# Número entero N > 0
# Factorial = producto de todos los enteros X tales que 0 < X <= N
# Osea, 1 * 2 * 3 * 4 * 5 * 6 * .... N

# Solicito N
# Rechazar si N < 0
# Calcular factorial
# Imprimir

N = -1

while(N <= 0):
    N = int(input("Ingrese un número>"))

Factorial = 1

Contador = 1
while(Contador <= N):
    Factorial *= Contador 
    Contador += 1

print("El factorial de", N, "es", Factorial)