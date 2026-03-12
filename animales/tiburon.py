from animales.pez import Pez


class Tiburon(Pez):

    def __str__(self):
        return f"Tiburón | {self.datos()}"
