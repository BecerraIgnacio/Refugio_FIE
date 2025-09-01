from persona import Persona
from pajaro import Pajaro
from perro import Perro
from gato import Gato

class Adoptante(Persona):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self.adoptados = set()
        
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}'

    def get_adoptados(self):
        for adoptado in self.adoptados:
            print(adoptado)

    def add_adoptado(self, adoptado):
        self.adoptados.add(adoptado)

    def remove_adoptado(self, adoptado):
        self.adoptados.remove(adoptado)

    def verificar_adoptado(self, adoptado):
        cant_perros = 0
        cant_gatos = 0
        cant_pajaritos = 0
        for adoptado in self.adoptados:
            if isinstance(adoptado, Perro):
                cant_perros += 1
            if isinstance(adoptado, Gato):
                cant_gatos+=1
            if isinstance(adoptado, Pajaro):
                cant_pajaritos+=1
        if cant_perros < 3 and cant_gatos < 2 and cant_pajaritos < 1:
            return False
        return True

