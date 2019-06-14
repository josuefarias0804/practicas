import datetime

class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion='', padre=None, hijos=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion
        self.padre = padre
        self.hijos = hijos

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
        #devolver el hijo mayor, si no hay ninguno devolver None
        pass

class Profesional(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion, padre=None, hijos=[], cuil=''):
        super().__init__(nombre, apellido, fecha_nacimiento, profesion, padre=padre, hijos=hijos)
        self.cuil = cuil

    def decir_hola(self):
        print('Hola!, Soy un profesional y me llamo ' + self.nombre_completo() + '. Mi cuil es ' + self.cuil)

class Menor(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, padre=None, hijos=[]):
        super().__init__(nombre, apellido, fecha_nacimiento, padre=padre, hijos=hijos)

    def agregar_hijo(self, hijo):
        print("Un menor no puede tener hijos")


'''persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero', None, [])
print(persona.decir_hola())
profesional = Profesional('Victor', 'Gutierrez', datetime.date(1999, 10, 1), 'abogado', None, [], '23456778')
print(profesional.decir_hola())'''

persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero')

persona.agregar_hijo(Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero'))
persona.agregar_hijo(Persona('Lucas', 'Lopez', datetime.date(1994, 5, 4), 'carpintero'))
menor = Menor('Mateo', 'Gonzalez', datetime.date(2010, 11, 3), None, [])

print(menor.agregar_hijo(Persona('Lucas', 'Lopez', datetime.date(1994, 5, 4))))

print('Cantidad de hijos: ' + str(persona.cant_hijos()))

