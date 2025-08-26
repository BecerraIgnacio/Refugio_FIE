from pajaro import Pajaro
from gato  import Gato
from perro import Perro
from datetime import date
from adoptante import Adoptante
def main():
    piolin = Pajaro("Piolin", date.today(), 1)
    piolin.saludar()
    mela = Gato("Mela", date(2023, 10, 20), 2)
    krypto = Perro("Krypto", date(2025, 8, 10), 3)
    mela.saludar()
    krypto.saludar()


if __name__ == '__main__':
    main()