# CargaDatos/GestionErrores.py
class GestionErrores:
    def __init__(self):
        self.errores = []  # Lista para almacenar errores

    def mostrar_formulario(self):
        print("Gestión de errores: revise los errores pendientes.")

    def gestionar_errores(self):
        while self.errores:
            print("Errores pendientes:")
            # Lógica para seleccionar y borrar errores
            error_actual = self.errores.pop(0)  # Ejemplo: borrar el primer error
            print(f"Error '{error_actual}' borrado. ¿Está seguro?")
        print("Todos los errores han sido gestionados y corregidos.")

if __name__ == "__main__":
    ge = GestionErrores()
    ge.mostrar_formulario()
    # Simulación: agregamos algunos errores y los gestionamos
    ge.errores = ["Error1", "Error2"]
    ge.gestionar_errores()
