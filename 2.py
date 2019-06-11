def precio_total(cant):
    precio_unit_fijo = 5.50
    return cant * precio_unit_fijo


cantidades = [5, 10, 100]

i = 0
while i < 3:
    print(precio_total(cantidades[i]))
    i += 1


for cant in cantidades:
    print(precio_total(cant))
