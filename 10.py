lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
lista_b = []

for elemento in lista_a:
    if elemento > 5:
        lista_a = elemento * 2
        lista_b.append(lista_a)

print(lista_b)




# recorrerlo con foreach, mostrar solo los valores mayores a 5 multiplicados x 2
