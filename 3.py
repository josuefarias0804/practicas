def precio_total(cant=5, precio=5.5):
    total = precio * cant
    return total


print(precio_total())
print(precio_total(10))
print(precio_total(precio=15.60))


def imprimir_cantidades(lista_de_cantidades_y_precios=[]):
    for cantidad, precio in lista_de_cantidades_y_precios:
        print(precio_total(cantidad, precio))


imprimir_cantidades()
