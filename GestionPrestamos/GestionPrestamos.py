# GestionPrestamos/GestionPrestamos.py
class GestionPrestamos:
    def __init__(self):
        pass

    def gestionar_prestamos(self):
        print("Mostrando alumnos filtrados para gestión de préstamos.")
        alumno_id = 1  # Ejemplo: alumno seleccionado
        print(f"Mostrando datos del alumno con ID: {alumno_id} y sus libros en préstamo.")
        print("Modificando estado de los libros...")
        # Lógica para actualizar estado y cerrar el préstamo
        print("Préstamo cerrado y contrato de cierre generado.")

if __name__ == "__main__":
    gp = GestionPrestamos()
    gp.gestionar_prestamos()
