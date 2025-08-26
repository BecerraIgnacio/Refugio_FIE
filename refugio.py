from adoptante import Adoptante
from persona import Persona
from transito import Transito
from mascota import Mascota

class Refugio:
    def __init__(self):
        self.lista_adoptante = set()
        self.lista_transito = set()
        self.lista_perros = set()
        self.lista_gatos = set()
        self.lista_pajaros =set()

    def agregar_adoptante(self, adoptante):
        self.lista_adoptante.add(adoptante)

    def eliminar_adoptante(self, adoptante):
        self.lista_adoptante.remove(adoptante)

    def listar_adoptantes(self):
        for adoptante in self.lista_adoptante:
            print(adoptante)

    def agregar_perro(self, perro):
        self.lista_perros.add(perro)

    def eliminar_perro(self, perro):
        self.lista_perros.remove(perro)

    def listar_perro(self):
        for perro in self.lista_perros:
            perro.saludar()

    def agregar_gato(self, gato):
        self.lista_gatos.add(gato)

    def eliminar_gato(self, gato):
        self.lista_gatos.remove(gato)

    def listar_gato(self):
        for gato in self.lista_gatos:
            gato.saludar()
    def agregar_pajaro(self, pajaro):
        self.lista_pajaros.add(pajaro)

    def eliminar_pajaro(self, pajaro):
        self.lista_pajaros.remove(pajaro)

    def listar_pajaro(self):
        for pajaro in self.lista_pajaros:
            pajaro.saludar()