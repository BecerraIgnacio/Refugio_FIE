from adoptante import Adoptante
from perro import Perro
from pajaro import Pajaro
from gato import Gato

class Adoptante_benefactor(Adoptante):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)
        self.adoptados = set()

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Cantidad de adoptados: {len(self.adoptados)}'

    def get_adoptados(self):
        for adoptado in self.adoptados:
            print(adoptado)

    def add_adoptado(self, adoptado):
        self.adoptados.add(adoptado)

    def remove_adoptado(self, adoptado):
        self.adoptados.remove(adoptado)

    def verificar_adoptado(self, adoptado):
        pass