from animales.animal import Animal


class Pez(Animal):

    def __str__(self):
        return f"Pez -> {self.datos()}"
