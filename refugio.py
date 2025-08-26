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
