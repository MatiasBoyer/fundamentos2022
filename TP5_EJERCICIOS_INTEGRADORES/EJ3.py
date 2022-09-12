# Empresa X aplica el siguiente procedimiento en la comercialización
# Unidades 1 <= X <= 12     : precio base
# Unidades 13 <= X <= 100   : 10% descuento
# Unidades 100 < X          : 25% descuento

# Bucle:
#   Solicitar cantidad de un producto
#   (si cantidad == -1, salir)
#   Solicitar precio base del producto
# Mostrar:
#   Cantidad total de ventas
#   Cantidad de ventas con 10% de descuento
#   Cantidad de ventas en las que se aplicó el precio base (sin descuentos)


# Para ser 100% honesto
# esto está horrible

# Probar con:
#   Q = 12, 13, 14, 99, 100, 101

VENTASTOTALES = 0
VENTASCON10DTO = 0
VENTASPRECIOBASE = 0

SALIR = 0
while(SALIR == 0):
    CANTIDAD = int(input("Ingrese cantidad de productos>"))
    if(CANTIDAD == -1):
        SALIR = 1
    else:
        PRECIOBASE = int(input("Ingrese precio base del producto>"))

        XPRECIOBASE = 0
        X10DTO = 0
        X25DTO = 0

        CONTADOR = 0
        while(CONTADOR < CANTIDAD):
            if (CONTADOR < 12): # Precio base
                XPRECIOBASE += 1
            elif (12 <= CONTADOR and CONTADOR <= 100): # 10% dto
                X10DTO += 1
            else: # 25% dto
                X25DTO += 1

            CONTADOR += 1

        VENTASTOTALES += XPRECIOBASE + X10DTO + X25DTO
        VENTASCON10DTO += X10DTO
        VENTASPRECIOBASE += XPRECIOBASE


print ("Total de ventas realizadas:", VENTASTOTALES)
print ("Total de ventas realizadas al 10 de descuento:", VENTASCON10DTO)
print ("Total de ventas realizadas a precio base:", VENTASPRECIOBASE)