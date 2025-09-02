from mascota import Mascota

class Gato(Mascota):
    def __init__(self, apodo, fecha_de_ingreso, id):
        super().__init__(apodo, fecha_de_ingreso, id)
        self.rehabilitacion = 360
        self.ruido = "Miau"
        self.tipo = "Gato"