from mascota import Mascota

class Perro(Mascota):
    def __init__(self, apodo, fecha_de_ingreso, id):
        super().__init__(apodo, fecha_de_ingreso, id)
        self.rehabilitacion = 30
        self.ruido = "Guau"
        self.tipo = "Perro"