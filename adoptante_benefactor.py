from adoptante import Adoptante
from perro import Perro
from pajaro import Pajaro
from gato import Gato

class Adoptante_benefactor(Adoptante):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Cantidad de adoptados: {len(self.adoptados)}'

    def verificar_adoptado(self):
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
            return True
        return False