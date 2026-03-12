from animales.animal import Animal


class Reptil(Animal):

    def __str__(self):
        return f"Reptil -> {self.datos()}"
