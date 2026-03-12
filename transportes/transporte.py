class Transporte:

    def __init__(self, marca_transporte):
        self.__marca_transporte = marca_transporte

    @property
    def marca_transporte(self):
        return self.__marca_transporte

    @marca_transporte.setter
    def marca_transporte(self, nueva_marca):
        self.__marca_transporte = nueva_marca

    def descripcion(self):
        return f"Marca del transporte: {self.__marca_transporte}"

    def __str__(self):
        return self.descripcion()
