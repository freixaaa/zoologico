from animales.mamifero import Mamifero


class Leon(Mamifero):

    def __str__(self):
        return f"León del zoológico | {self.datos()}"
