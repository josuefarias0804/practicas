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
        i=0
        lista_edades = []
        todas_edades = []
        edad_personas = None
        personas = None
        maximo = None
        for elemento in self.hijos:             # recorré la lista de hijos [(laura), (matias)]
            personas = elemento                 # persona1 (laura) -- luego persona2 (matias)
            lista_edades.append(personas)       # lista_edades = persona1(laura) -- luego persona2(matias)
            edad_personas = personas.edad()     # edad_personas = 18 (edad de laura) -- luego 14 (edad de matias)
            todas_edades.append(edad_personas)  # todas_edades = [18] -- luego [18, 14]
            maximo = max(todas_edades)          # maximo = 18
        if edad_personas == maximo:             # si 18 = 18     -- luego si 14 = 18
            return personas
            # devolvé persona1(laura)
        else:                                   # sino
            return personas                     # devolvé persona1(laura)



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
persona.agregar_hijo(Menor('Laura', 'Lopez', datetime.date(2000, 10, 1), 'carpintero'))
persona.agregar_hijo(Menor('Matias', 'Lopez', datetime.date(2005, 10, 1), 'carpintero'))


otra_persona = Persona('Carlos', 'Lopez', datetime.date(1999, 10, 1), 'carpintero')
print(otra_persona.hijo_mayor())

print(f'Mi hijo mayor se llama {persona.hijo_mayor().nombre_completo()}')



print('Cantidad de hijos: ' + str(persona.cant_hijos()))









# hijoMayor

