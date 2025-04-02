# GestionListados/GestionListados.py
class GestionListados:
    def __init__(self):
        pass

    def generar_listado_alumnos(self, formato):
        print(f"Generando listado de alumnos en formato {formato}.")
        # Lógica para generar el fichero del listado

    def generar_otro_listado(self, listado, formato):
        print(f"Generando listado '{listado}' en formato {formato}.")
        # Lógica para generar otro tipo de listado

if __name__ == "__main__":
    gl = GestionListados()
    gl.generar_listado_alumnos("PDF")
    gl.generar_otro_listado("Cursos", "CSV")
