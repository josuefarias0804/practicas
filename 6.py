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

    def edad(self):
        today = date.today()
        return today.year - self.fecha_nacimiento.year - ((today.month, today.day) < (self.fecha_nacimiento.month,
                                                                                      self.fecha_nacimiento.day))


persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero')

print('La profesion de ' + persona.nombre_completo() + ' es ' + persona.profesion + ' y tiene ' + str(persona.edad())
      + ' años')
