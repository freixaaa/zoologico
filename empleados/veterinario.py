from empleados.empleado import Empleado


class Veterinario(Empleado):

    def __init__(self, nombre_persona, edad_persona):
        super().__init__(nombre_persona, edad_persona)

    def __str__(self):
        return f"[Veterinario] {self.informacion()}"
