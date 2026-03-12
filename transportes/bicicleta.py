from transportes.transporte import Transporte


class Bicicleta(Transporte):

    def __str__(self):
        return f"Bicicleta | {self.descripcion()}"
