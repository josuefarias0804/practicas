import datetime
from datetime import date

class Persona:

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion

    def nombre_completo(self):
        return self.nombre + " " + self.apellido

    def calculate_age(born):
        today = date.today()
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero')
edad = Persona
edad1 = edad.calculate_age(datetime.date(1999, 10, 1))

print('La profesion de ' + persona.nombre_completo() + ' es ' + persona.profesion + ' y tiene ' + str(edad1) + ' años')
