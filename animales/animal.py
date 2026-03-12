class Animal:

    def __init__(self, nombre_animal):
        self.__nombre_animal = nombre_animal

    @property
    def nombre_animal(self):
        return self.__nombre_animal

    @nombre_animal.setter
    def nombre_animal(self, nuevo_nombre):
        self.__nombre_animal = nuevo_nombre

    def datos(self):
        return f"Animal registrado: {self.__nombre_animal}"

    def __str__(self):
        return self.datos()
