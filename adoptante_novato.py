from adoptante import Adoptante

class Adoptante_novato(Adoptante):
    def __init__(self, nombre, apellido, dni):
        super().__init__(nombre, apellido, dni)

    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Cantidad de adoptados: {len(self.adoptados)}'

    def verificar_adoptado(self):
        if len(self.adoptados) > 0:
            return False
        else:
            return True