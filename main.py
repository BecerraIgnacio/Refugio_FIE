from pajaro import Pajaro
from gato  import Gato
from perro import Perro
from datetime import date
from adoptante import Adoptante
from adoptante_novato import Adoptante_novato
from adoptante_benefactor import Adoptante_benefactor
from refugio import Refugio


def main():
    refugio = Refugio()
    piolin = Pajaro("Piolin", date.today(), 1)
    piolin.saludar()
    mela = Gato("Mela", date(2023, 10, 20), 2)
    krypto = Perro("Krypto", date(2025, 8, 10), 3)
    mela.saludar()
    krypto.saludar()
    adoptante1 = Adoptante_benefactor("juani", "gone", 45819720)
    adoptante2 = Adoptante_novato("ignacio", "bbto", 42933087)

    refugio.agregar_adoptante(adoptante1)
    refugio.agregar_adoptante(adoptante2)
    refugio.listar_adoptantes()
    refugio.eliminar_adoptante(adoptante1)
    refugio.listar_adoptantes()




if __name__ == '__main__':
    main()