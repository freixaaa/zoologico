from transportes.transporte import Transporte


class Cuadraciclo(Transporte):

    def __str__(self):
        return f"Cuadraciclo | {self.descripcion()}"
