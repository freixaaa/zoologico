from animales.reptil import Reptil


class Iguana(Reptil):

    def __str__(self):
        return f"Iguana | {self.datos()}"
