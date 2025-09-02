class Adopcion:
    def __init__(self, adoptante, mascota):
        self.adoptante = adoptante
        self.mascota = mascota

    def __str__(self):
        return self.mascota.get_apodo() + " fue adoptado por " + self.adoptante.get_nombre()
