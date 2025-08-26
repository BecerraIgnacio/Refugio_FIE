from persona import Persona

class Tipo_adoptante:
    ADOPTANTE_NOVATO = "adoptante_novato"
    ADOPTANTE_BENEFACTOR = "adoptante_benefactor"

class Adoptante(Persona):
    def __init__(self, nombre, apellido, dni, tipo_de_adoptante):
        super().__init__(nombre, apellido, dni)
        self.tipo_de_adoptante = Tipo_adoptante.ADOPTANTE_NOVATO
        adoptados = set()
        
    def __str__(self):
        return f'Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}, Tipo de adoptante: {self.tipo_de_adoptante}'
    


