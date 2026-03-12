from animales.ave import Ave


class Aguila(Ave):

    def __str__(self):
        return f"Águila | {self.datos()}"
