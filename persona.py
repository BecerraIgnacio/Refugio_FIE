class Persona:

    def __init__(self, nombre, apellido, dni):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni

    def __str__(self):
        return f'Nombre: {self.nombre} {self.apellido}, DNI: {self.dni}'

    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_dni(self):
        return self.dni