from datetime import date


persona = {
    'nombre': 'Carlos',
    'apellido': 'Lopez',
    'fecha_nacimiento': date(1999, 10, 1),
}


def imprimir_nombres(*args):
    for nombre in args:
        print(nombre)


imprimir_nombres('Luis', 'Pedro', 'Carlos')


def actualizar_persona(persona, **kwargs):
    for arg in kwargs:
        if arg not in ['nombre', 'apellido', 'fecha_nacimiento', 'profesion']:
            raise ValueError(f'Argumento invalido para persona: "{arg}"')
        persona[arg] = kwargs[arg]


actualizar_persona(persona, nombre='Claudio')
print(persona)