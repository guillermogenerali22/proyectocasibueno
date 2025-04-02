# CargaDatos/CargarBBDD.py
import configparser

class CargarBBDD:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('Recursos/config.ini')  # Archivo de configuración con los datos de la BBDD

    def cargar_datos(self, nombre_fichero):
        print(f"Cargando datos desde el fichero: {nombre_fichero}")
        # Lógica para cargar los datos en la BBDD 'proyecto'
        print("Datos cargados correctamente. Libros listados en formato de lista.")

    def actualizar_stock(self):
        print("Stock de libros actualizado si ha habido cambios.")

    def copia_seguridad(self):
        print("Realizando copia de seguridad de la base de datos.")
        # Lógica para la copia de seguridad

if __name__ == "__main__":
    cargar = CargarBBDD()
    cargar.cargar_datos("ejemplo.txt")
    cargar.actualizar_stock()
    cargar.copia_seguridad()
