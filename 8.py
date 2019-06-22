import datetime
from datetime import date

class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion='', padre=None, hijos=None):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion
        self.padre = padre
        self.hijos = hijos or []

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def decir_hola(self):
        print('Hola! soy una persona y me llamo ' + self.nombre_completo())

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)

    def cant_hijos(self):
        return len(self.hijos)

    def hijo_mayor(self):
        hijoMayor = None

        for hijo in self.hijos:
            if hijoMayor is None:
                hijoMayor = hijo
                if hijoMayor.fecha_nacimiento <= hijo.fecha_nacimiento:
                    hijoMayor = hijo
            else:
                if hijoMayor.fecha_nacimiento < hijo.fecha_nacimiento:
                    hijoMayor = hijoMayor
                else:
                    hijoMayor = hijo
        return hijoMayor

    def tiene_hijo_con_nombre(self, nombre):
        nombre_hijo = None
        for hijo in self.hijos:
            if nombre_hijo == None:
                nombre_hijo = hijo.nombre
                if nombre_hijo == nombre:
                    return True
                else:
                    nombre_hijo = ''
            else:
                if hijo.nombre == nombre:
                    return True
                else:
                    nombre_hijo = hijo.nombre
        return False



    def hijo_menor_edad(self, nombre):
        hijo_menor_ed = None
        for hijo in self.hijos:
            if hijo_menor_ed == None:
                hijo_menor_ed = hijo
                if hijo.nombre == nombre:
                    if hijo.edad() < 18:
                        return 'es menor de edad'
                    else:
                        return 'no es menor de edad'
            else:
                if hijo.nombre == nombre:
                    if hijo.edad() < 18:
                        return 'es menor de edad'
                    else:
                        return 'no es menor de edad'


    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month,
                                                                                      self.fecha_nacimiento.day))


class Profesional(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion, padre=None, hijos=None, cuil=''):
        super().__init__(nombre, apellido, fecha_nacimiento, profesion, padre=padre, hijos=hijos)
        self.cuil = cuil

    def decir_hola(self):
        print('Hola!, Soy un profesional y me llamo ' + self.nombre_completo() + '. Mi cuil es ' + self.cuil)

class Menor(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, padre=None, hijos=None):
        super().__init__(nombre, apellido, fecha_nacimiento, padre=padre, hijos=hijos)

    def agregar_hijo(self, hijo):
        print("Un menor no puede tener hijos")


'''persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero', None, [])
print(persona.decir_hola())
profesional = Profesional('Victor', 'Gutierrez', datetime.date(1999, 10, 1), 'abogado', None, [], '23456778')
print(profesional.decir_hola())'''


persona = Persona('Carlos', 'Lopez', datetime.date(1990, 10, 1), 'carpintero')
persona.agregar_hijo(Menor('Nadia', 'Lopez', datetime.date(1984, 10, 1), 'carpintero'))
persona.agregar_hijo(Menor('Laura', 'Lopez', datetime.date(2000, 10, 1), 'carpintero'))
persona.agregar_hijo(Menor('Matias', 'Lopez', datetime.date(2005, 10, 1), 'carpintero'))
persona.agregar_hijo(Menor('Ariel', 'Lopez', datetime.date(1988, 10, 1), 'carpintero'))
persona.agregar_hijo(Menor('Marta', 'Lopez', datetime.date(1974, 10, 1), 'carpintero'))
persona.agregar_hijo(Menor('Dante', 'Lopez', datetime.date(1986, 10, 1), 'carpintero'))
otra_persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero')
otra_persona.agregar_hijo(Menor('Cristian', 'Saavedra', datetime.date(1990, 11, 2), 'carpintero'))


print(f'Tengo un hijo con ese nombre (True/False): {str(persona.tiene_hijo_con_nombre("Luis"))}')   # Lo convertí a string para concatenar la frase y que quede mejor
print(f'Mi hijo mayor se llama {persona.hijo_mayor().nombre_completo()}')
print(f'Soy otra persona y mi hijo mayor se llama {otra_persona.hijo_mayor().nombre_completo()}')
print(f'Cantidad de hijos: {str(persona.cant_hijos())}')
print(f'Mi hijo {persona.hijo_menor_edad("Nadia")}')











