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

    def decir_hola(self):
        print('Hola! soy una persona y me llamo ' + self.nombre_completo())

    def agregar_hijo(self, hijo):
        self.hijo = self.padre
        return self.padre

class Profesional(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, profesion, padre=None, hijos=[], cuil):
        super(Profesional, self).__init__(self, nombre, apellido, fecha_nacimiento, profesion, padre=None, hijos=[])
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.profesion = profesion
        self.padre = padre
        self.hijos = hijos
        self.cuil = cuil

    def decir_hola(self):
        print('Hola!, Soy un profesional y me llamo ' + self.nombre_completo() + '. Mi cuil es ' + self.cuil)

class Menor(Persona):

    def __init__(self, nombre, apellido, fecha_nacimiento, padre=None, hijos=[], cuil):
        super(Menor, self).__init__(self, nombre, apellido, fecha_nacimiento, padre=None, hijos=[], cuil)
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nacimiento = fecha_nacimiento
        self.padre = padre
        self.hijos = hijos
        self.cuil = cuil

    def agregar_hijo(self, hijo):
        print('Un menor no puede tener hijos')


persona = Persona('Carlos', 'Lopez', '12/12/1999', 'carpintero', None, [])
print(persona.decir_hola())
profesional = Profesional('Victor'. 'Gutierrez', '12/09/1988', 'abogado', None, [], '23456778')
print(profesional.decir_hola())
