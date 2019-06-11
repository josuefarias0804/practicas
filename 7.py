import datetime
from datetime import date

class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion, padre, hijos=[]):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion
        self.padre = padre
        self.hijos = hijos

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

    def agregar_hijo(self, hijo, padre):
        self.hijo 
        return hijo

persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero', None, [])
edad = Persona
edad1 = edad.calculate_age(datetime.date(1999, 10, 1))

print('La profesion de ' + persona.nombre_completo() + ' es ' + persona.profesion + ' y tiene ' + str(edad1) + ' años')
