from persona import Persona

class Animal_transito:
    PERRO = "perro"
    GATO = "gato"
    PAJARO = "pajaro"

class Transito(Persona):
    def __init__(self, nombre, apellido, dni, animal_transito):
        super().__init__(nombre, apellido, dni)
        if animal_transito not in (Animal_transito.PAJARO, Animal_transito.GATO, Animal_transito.PERRO):
            raise ValueError("No se puede hacer transito a esos animales.")

    self.animal_transito = animal_transito
    animales_en_transito = set()
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, DNI: {self.dni}.\nAnimales que transita: {self.animal_transito}, Cantidad en transito: {len(self.cantidad_en_transito)}"

        