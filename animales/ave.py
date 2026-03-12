from animales.animal import Animal


class Ave(Animal):

    def __str__(self):
        return f"Ave -> {self.datos()}"
