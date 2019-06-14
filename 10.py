lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

i=0

for i in range(0, len(lista_a)):
    if lista_a[i] > 5:
        lista_a[i] = lista_a[i]*2
    i+1
print(lista_a)
