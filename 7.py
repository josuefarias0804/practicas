import datetime
from datetime import date

class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion, padre=None, hijos=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion
        self.padre = padre
        self.hijos = hijos

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month,
                                                                                      self.fecha_nacimiento.day))

    def agregar_hijo(self, hijo):
        hijo.padre = self
        self.hijos.append(hijo)



persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero', None, [])
persona.agregar_hijo(Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero'))
persona.agregar_hijo(Persona('Lucas', 'Lopez', datetime.date(1994, 5, 4), 'carpintero'))

print('La profesion de ' + persona.nombre_completo() + ' es ' + persona.profesion + ' y tiene ' + str(persona.edad()) + ' años')