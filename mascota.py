from datetime import date

class Mascota:
    def __init__(self, apodo, fecha_de_ingreso, id):
        self.apodo = apodo
        self.fecha_de_ingreso = fecha_de_ingreso
        self.id = id

    def is_rehabilitado(self):
        return (date.today() - self.fecha_de_ingreso).days >= self.rehabilitacion

    def saludar(self):
        if self.is_rehabilitado():
            print(f"{self.apodo} dice {self.ruido}")
            return
        print(f"{self.apodo} no fue rehabilitado aun")

    def __str__(self):
        print(f"{self.apodo} es un {self.tipo}")

    def get_apodo(self):
        return self.apodo

    def get_fecha_de_ingreso(self):
        return self.fecha_de_ingreso

    def get_id(self):
        return self.id