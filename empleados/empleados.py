    class Empleado:

    def __init__(self, nombre_persona, edad_persona):
        self.__nombre_persona = nombre_persona
        self.__edad_persona = edad_persona

    @property
    def nombre_persona(self):
        return self.__nombre_persona

    @nombre_persona.setter
    def nombre_persona(self, nuevo_nombre):
        self.__nombre_persona = nuevo_nombre

    @property
    def edad_persona(self):
        return self.__edad_persona

    @edad_persona.setter
    def edad_persona(self, nueva_edad):
        self.__edad_persona = nueva_edad

    def informacion(self):
        return f"{self.__nombre_persona} ({self.__edad_persona} años)"

    def __str__(self):
        return self.informacion()
        
