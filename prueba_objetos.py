class Persona():
    def init(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def str(self):
        return (f"Nombre {self.nombre}, {self.edad} años")
class Estudiante(Persona):
    def init(self, nombre, edad, carrera, curso):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.curso = curso
    def str(self):
        return (f"nombre {self.nombre}, {self.edad} años, {self.carrera} carrera, {self.curso} curso")
estudiante=Estudiante("Juanito", 19, "Ingenieria", "cuarto")
class Empleado(Persona):
    def init(self, nombre, edad, dni, salario):
        Persona(self, nombre, edad)
        self.dni = dni
        self.salario = salario
    def str(self):
        return Persona.str(self)+ (f"{self.dni} dni, {self.salario} euros")
empleado=Empleado("Jose", 24, "65639215R", 40000)
class Delegado(Persona):
    def init(self, nombre, edad, carrera, curso, asignatura):
        Persona(self, nombre, edad, carrera, curso)
        self.asignatura = asignatura
    def str(self):
        return Persona.str(self)+ (f"{self.asignatura} asignatura")
delegado=Delegado("Carlos", 28, "ADE", "sexto", "Matematicas")
class Profesor(Persona):
    def init(self, nombre, edad, dni, salario, asignatura, oficina):
        Persona(self, nombre, edad, dni, salario)
        self.asignatura = asignatura
        self.oficina = oficina
        return Persona.str(self)
profesor=Profesor("Alvaro", 30, "54197854L", 50000, "Matematicas" , 4)

def Catalogar(personas,edad):
    for i in personas:
        if i.edad == edad:
            print(type(i)._name_, i)
personas = [Estudiante("Juanito", 19, "Ingenieria", "cuarto"), Empleado("Jose", 24, "65639215R", 40000), Delegado("Carlos", 28, "ADE", "sexto", "Matematicas"), Profesor("Alvaro", 30, "54197854L", 50000, "Matematicas" , 4)
Catalogar(personas,19)
