from adoptante import Adoptante

class Adoptante_novato(Adoptante):
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
        if len(adoptado) > 0:
            return False
        else:
            return True