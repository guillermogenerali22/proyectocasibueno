# GestionAlumnos/FiltrarAlumnos.py
class FiltrarAlumnos:
    def __init__(self):
        self.filtro = None

    def mostrar_alumnos_sin_filtrar(self):
        print("Mostrando lista de alumnos sin filtrar.")

    def cambiar_filtro(self, nuevo_filtro):
        self.filtro = nuevo_filtro
        print(f"Filtro cambiado a: {self.filtro}")
        # Lógica para mostrar los alumnos filtrados

if __name__ == "__main__":
    filtro = FiltrarAlumnos()
    filtro.mostrar_alumnos_sin_filtrar()
    filtro.cambiar_filtro("Apellido inicial A-M")
