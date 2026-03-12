from transportes.transporte import Transporte


class Patineta(Transporte):

    def __str__(self):
        return f"Patineta | {self.descripcion()}"
