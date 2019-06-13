import datetime
x = datetime.date(1999, 10, 1)
diccionario = {'nombre': 'Carlos', 'apellido': 'Lopez', 'fecha_nacimiento' : x}


print(diccionario['nombre'])

diccionario['nombre'] = 'Luis'
diccionario['profesion'] = 'Carpintero'


def nombre_completo(diccionario):
    return(diccionario['nombre']) + ' ' +  (diccionario[('apellido')])

print(nombre_completo(diccionario))

print(f'La profesión de {nombre_completo(diccionario)} es {diccionario["profesion"]}')

