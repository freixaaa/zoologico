from animales.animal import Animal


class Mamifero(Animal):

    def __str__(self):
        return f"Mamífero -> {self.datos()}"
