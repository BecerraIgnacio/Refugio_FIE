from adoptante import Adoptante
from persona import Persona
from transito import Transito
from mascota import Mascota
from adopcion import Adopcion

class Refugio:
    def __init__(self):
        self.lista_adoptante = set()
        self.lista_transito = set()
        self.lista_mascotas = set()
        self.lista_adopciones = set()

    def agregar_adoptante(self, adoptante):
        self.lista_adoptante.add(adoptante)

    def eliminar_adoptante(self, adoptante):
        self.lista_adoptante.remove(adoptante)

    def listar_adoptantes(self):
        for adoptante in self.lista_adoptante:
            print(adoptante)

    def agregar_mascota(self, mascota):
        self.lista_mascotas.add(mascota)

    def eliminar_mascota(self, mascota):
        self.lista_mascotas.remove(mascota)

    def listar_mascotas(self):
        for mascota in self.lista_mascotas:
            mascota.saludar()


    def adoptar_mascota(self, adoptante, mascota):
        if mascota in self.lista_mascotas:
            if adoptante in self.lista_adoptante:
                if mascota.is_rehabilitado():
                    if adoptante.verificar_adoptado():
                        adoptante.add_adoptado(mascota)
                        self.eliminar_mascota(mascota)
                        self.lista_adopciones.add(Adopcion(adoptante, mascota))
                        return
                    print("Este adoptante ya adopto su maximo de mascotas.")
                    return
                print(f"{mascota.get_apodo()} no fue rehabilitado aun")
                return
            print("Este adoptante no pertenece al refugio")
            return
        print("Esta mascota no pertenece al refugio")


    def listar_adopciones(self):
        for adopcion in self.lista_adopciones:
            print(adopcion)
