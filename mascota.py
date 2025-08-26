from datetime import date
class Mascota:
    def __init__(self, apodo, fecha_de_ingreso, id):
        self.apodo = apodo
        self.fecha_de_ingreso = fecha_de_ingreso
        self.id = id

    def saludar(self):
        if(date.today() - self.fecha_de_ingreso).days >= self.rehabilitacion:
            print(f"{self.apodo} dice {self.ruido}")
            return
        print(f"{self.apodo} no fue rehabilitado aun")
