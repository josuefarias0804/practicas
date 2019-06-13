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
        return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


class ObjetoConCuil:

    def __init__(self, cuil):
        self.cuil = cuil

    def imprimir_documento(self):
        print(self.cuil)

class Profesional(ObjetoConCuil, Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion, cuil):
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion
        self.cuil = cuil

class Proveedor(ObjetoConCuil):
    def __init__(self, cuil):
        self.cuil = cuil


profesional1 = Profesional('Carlos', 'Lopez', '10/05/1991', 'carpintero', '20343219262')
profesional1.imprimir_documento()
proveedor1 = Proveedor('2034321926')
proveedor1.imprimir_documento()




