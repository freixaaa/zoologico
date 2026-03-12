from animales.anfibio import Anfibio


class Rana(Anfibio):

    def __str__(self):
        return f"Rana | {self.datos()}"
