from mascota import Mascota

class Pajaro(Mascota):
    def __init__(self, apodo, fecha_de_ingreso, id):
        super().__init__(apodo, fecha_de_ingreso, id)
        self.rehabilitacion = 0
        self.ruido = "Pio"
        self.tipo = "Pajaro"
