from empleados.empleado import Empleado


class Guardian(Empleado):

    def __init__(self, nombre_persona, edad_persona):
        super().__init__(nombre_persona, edad_persona)

    def __str__(self):
        return f"[Guardia de zoológico] {self.informacion()}"
