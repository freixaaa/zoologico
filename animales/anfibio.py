from animales.animal import Animal


class Anfibio(Animal):

    def __str__(self):
        return f"Anfibio -> {self.datos()}"
